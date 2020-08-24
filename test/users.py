import json
# json_string = [{"user": "Guido"}, {"user": "Rossum"}]
#
# # paserd_json = json.loads(json_string)
#
# for user in json_string:
#     print(user.values())
#
# list_name = list()
#
# for i in range(0, 2):
#     name = input("name")
#     list_name.append(name)
#
# print(list_name)

# list_ambiente = [{'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args':
#     ['/bin/bash', 'resources/pipeline/deploy/steps/validation/validate.sh', 'e2d', 'feature/SBOX-1508-update-the-topics-for-each-subject-in-the-budget-sandbox-monitoring'],
#                   'id': 'validation', 'timing': {'startTime': '2020-08-12T19:48:53.810488651Z', 'endTime': '2020-08-12T19:49:35.422105663Z'}
#                      , 'pullTiming': {'startTime': '2020-08-12T19:48:53.810488651Z', 'endTime': '2020-08-12T19:49:34.286226257Z'},
#                   'status': 'FAILURE'},
#                  {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy',
#                   'args': ['/bin/bash', 'resources/pipeline/deploy/steps/migration_postgres/backup.sh', 'e2d', 'y']
#                      , 'id': 'postgres_database_backup', 'waitFor': ['validation'], 'status': 'QUEUED'},
#                  {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args':
#                      ['/bin/bash', 'resources/pipeline/deploy/steps/migration_postgres/migrate.sh', 'e2d', 'y'], 'id': 'postgres_database_migration', 'waitFor':
#                      ['postgres_database_backup'], 'status': 'QUEUED'}, {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args':
#         ['/bin/bash', 'resources/pipeline/deploy/steps/migration_firestore/backup.sh', 'e2d', 'y', 'gs://sandbox-deployment-resources'],
#                                                                          'id': 'firestore_database_backup', 'waitFor': ['validation'], 'status': 'QUEUED'},
#                  {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args': ['/bin/bash', 'resources/pipeline/deploy/steps/migration_firestore/migrate.sh', 'e2d', 'y'],
#                   'id': 'firestore_database_migration', 'waitFor': ['firestore_database_backup'], 'status': 'QUEUED'}, {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args': ['/bin/bash', 'resources/pipeline/deploy/steps/frontend_build/frontend_build.sh', 'e2d'], 'id': 'frontend_build', 'waitFor': ['validation'], 'status': 'QUEUED'}, {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args': ['/bin/bash', 'resources/pipeline/deploy/steps/deploy_appengine/deploy_appengine.sh', 'e2d', 'feature/SBOX-1508-update-the-topics-for-each-subject-in-the-budget-sandbox-monitoring'], 'id': 'deploy_appengine', 'waitFor': ['frontend_build'], 'status': 'QUEUED'}, {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args': ['/bin/bash', 'resources/pipeline/deploy/steps/deploy_cloud_functions/deploy_cloud_functions.sh', 'e2d', 'y'], 'id': 'deploy_cloud_functions', 'waitFor': ['validation'], 'status': 'QUEUED'}, {'name': 'us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy', 'args': ['/bin/bash', 'resources/pipeline/deploy/steps/execute_warmup/execute_warmup.sh', 'e2d'], 'id': 'execute_warmup', 'waitFor': ['deploy_appengine'], 'status': 'QUEUED'}]
#
#
# #
# print(list_ambiente)

# LINK_DEPLOY = [
#     "us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy",
#     "us.gcr.io/budget-sandbox-dev/gcp_build_python"
# ]
#
# print(LINK_DEPLOY[1])

MESSAGE_PATTERN_BUILD = """
Build status: *{build_status}*

Build link: {build_link}
Commit link: {commit_link}
Branch or Tag name: {branch_name}
"""
#
# MESSAGE_PATTERN_BUILD.format(
#                 build_status="TESET",
#                 build_link="TEST",
#                 commit_link="TEST",
#                 branch_name="TEST")
#
# print(MESSAGE_PATTERN_BUILD)

TRIGGER_STEPS = [
    "us.gcr.io/budget-sandbox-dev/gcp_sandbox_deploy",
    "us.gcr.io/budget-sandbox-dev/gcp_build_python"
]

print(TRIGGER_STEPS[0])