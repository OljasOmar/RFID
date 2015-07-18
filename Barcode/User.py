
class User:

    def __init__(self, name, department, barcode_id):
        self.name = name
        self.department = department
        self.barcode_id = barcode_id

# import json
# def object_decoder(obj):
#     if '__type__' in obj and obj['__type__'] == 'User':
#         return User(obj['name'], obj['department'], obj['barcode_id'])
#     return obj
#
# json.loads("jsondy alyp kelu kerek"), object_hook=object_decoder)
#
# print user[name]
# print user[department]
# print user[barcode_id]
#

#>>>> <class '__restricted__.User'>