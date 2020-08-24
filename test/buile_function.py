"""Module to manager the notification."""
import base64
import json

import requests


VALID_BUILD_STATUS = [
    "SUCCESS",
    "FAILURE",
    "INTERNAL_ERROR",
    "TIMEOUT"
]

MESSAGE_PATTERN_BUILD = """
Build status: *{build_status}*

Build link: {build_link}
Commit link: {commit_link}
Branch or Tag name: *{branch_name}*
"""

MESSAGE_PATTERN_DEPLOY = """
Deploy status: *{build_status}

Environment: *{environment_deploy}
Build link: *{commit_link}
Branch: *{branch_name}
"""

COMMIT_PATTERN = "https://bitbucket.org/ciandt_it/google-budget-sandbox/commits/{}"

URL = (
    "https://chat.googleapis.com/v1/spaces/AAAApD2jiFs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3C"
    "PzqKqqsHI&token=jQ-_TegafFEnebwD92z2nfyH_rEio0uDIlUg4niypXM%3D"
)

TRIGGER_STEPS = {
    "deploy": "us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy",
    "build": "us.gcr.io/budget-sandbox-dev/gcp_build_python"
}

THREADS = {
    "deploy": "spaces/AAAApD2jiFs/threads/VkfZpZadZR8",
    "build": "spaces/AAAApD2jiFs/threads/gKZceb_sTU8"
}

RED_COLOR = "#FF0000"
GREEN_COLOR = "#008000"


def build_notification(event, context):
    """Build notification."""

    print(context)

    build_status = event["attributes"]["status"]

    if build_status in VALID_BUILD_STATUS:
        build_detail = get_build_details(event)
        trigger_steps = build_detail['steps'][0].get('name')

        print(build_detail)

        font_color = get_font_color(build_status)
        build_link = build_detail["logUrl"]
        commit_link = get_commit_pattern(build_detail)
        branch_name = build_detail["substitutions"].get("BRANCH_NAME")
        print(f"environment deploy:::: {build_detail['substitutions'].get('_ENV')}")

        if not branch_name:
            branch_name = build_detail["substitutions"].get("TAG_NAME")

        message = MESSAGE_PATTERN_BUILD.format(font_color=font_color,
                                         build_status=build_status,
                                         build_link=build_link,
                                         commit_link=commit_link,
                                         branch_name=branch_name)

        message = generate_steps_message(message, build_detail)
        print(message)

        payload = json.dumps({
            "text": message,
            "thread": get_thread(trigger_steps)
        })

        response = requests.post(URL, data=payload)
        print(response)


def get_thread(trigger_steps):
    """Get thread."""
    if trigger_steps == TRIGGER_STEPS.get("deploy"):
        return {"name": THREADS.get("deploy")}
    return {"name": THREADS.get("build")}


def get_font_color(build_status):
    """Get font color."""
    if build_status == "SUCCESS":
        return RED_COLOR
    return GREEN_COLOR


def get_build_details(event):
    """Get build details."""
    return json.loads(base64.b64decode(event["data"]).decode("utf-8"))


def get_commit_pattern(build_detail):
    """Get commit pattern."""
    return COMMIT_PATTERN.format(
        build_detail["sourceProvenance"]["resolvedRepoSource"]["commitSha"]
    )


def generate_steps_message(message, build_detail):
    """"Generate messages for steps."""

    for step in build_detail["steps"]:
        if step["status"] == "FAILURE":
            message += step["id"] + ": " + step["status"] + "\n"

    return message
