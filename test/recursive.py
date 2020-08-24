# houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
# #
# # def deliver_presents_recursively(houses):
# #     if len(houses) == 1:
# #         house = houses[0]
# #         print("Delivering present to", house)
# #
# #     else:
# #         mid = len(houses) // 2
# #         first_half = houses[:mid]
# #         second_half = houses[mid:]
# #
# #         deliver_presents_recursively(first_half)
# #         deliver_presents_recursively(second_half)
# #
# # deliver_presents_recursively(houses)
# #
# #
# # # payload = json.dumps({
# # #             "text": message,
# # #             "thread": {
# # #                 "name": "spaces/AAAApD2jiFs/threads/gKZceb_sTU8",
# # #                 "name": "spaces/AAAApD2jiFs/threads/VkfZpZadZR8"
# # #             }
# # #         })
# #
# # LINK_DEPLOY = [
# #     "us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy",
# #     "us.gcr.io/budget-sandbox-dev/gcp_build_python"
# # ]

THREADS = {
    "deploy": "spaces/AAAApD2jiFs/threads/VkfZpZadZR8",
    "build": "spaces/AAAApD2jiFs/threads/gKZceb_sTU8"
}

TRIGGER_STEPS = {
    "deploy": "us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy",
    "build": "us.gcr.io/budget-sandbox-dev/gcp_build_python"
}


def get_thread(trigger_steps):
    """Get thread."""
    if trigger_steps == TRIGGER_STEPS.get("deploy"):
        return {"name": THREADS.get("deploy")}
    return {"name": THREADS.get("build")}


# print({"name": THREADS.get("deploy")})
print({"name": THREADS.get("build")})

