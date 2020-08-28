# new_program_instance = {
#         "id": 74,
#         "instance_id": "PM56",
#         "program_id": "Program ID A",
#         "program_identifier": "test",
#         "program_name": "Program ID A test EMEA",
#         "sub_region": "EMEA"
#       },
#
# print(new_program_instance)


test =[{'options': [{'name': 'Infrastructure', 'id': 'infrastructure'}, {'id': 'readiness-enablement', 'name': 'Readiness/Enablement'}, {'id': 'tvc', 'name': 'TVC'}], 'field': 'non_program'}]


# print(test)
# print(test[0].get('options')[1].get('name'))

# name = list(filter(lambda name: name['options'], test))
#
# print(name)

for name in test:
        for v in name['options']:
                print(v.get("id"))



