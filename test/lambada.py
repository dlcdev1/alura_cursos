names = [{
    'id': 123,
    'name': 'David'
},
{
'id': 124,
'name': 'Paulo'
}]
# print(names[0].get('name'))

# for name in names:
#     print(name.get('name'))

# print(names)                           lambada.py:13
ids = 124

# client = list(filter(lambda x: del x['id'] == ids, names))
# print(client)

for index, cliente in enumerate(names):
    if cliente['id'] == ids:
        del(names[index])

print(list(names))
