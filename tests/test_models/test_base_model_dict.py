#!/usr/bin/python3
""" Test module for base model dictionary """

from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--------")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my model:")
for key in my_model_json.keys():
    print("\t{} : ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

print("---")
my_new_model = BaseModel(**my_model_json)
print(my_newmodel.id)
print(my_new_model)
print(type(my_new_model.create_at))

print("--")
print(my_model is my_new_model)

if __name__ == "__main__":
    unittest.main()
