import json

#+++++++++ loads +++++++++

#  json.loads are basically used for converting js string to pythomn dis  

# json_str =  '{"name": "Deep Kumar", "branch": "AIML"}'

# print(json_str)
# print(type(json_str))

# // convet into Python discnary
# json_object = json.loads(json_str)
# print(json_object)
# print(type(json_object))



#+++++++++ dumps +++++++++
# dis = {
#     "name": "Deep Kumar",
#     "branch": "AIML",
#     "hello" : None 
# }

# print(dis)
# print(type(dis))

# json_str = json.dumps(dis)
# print(json_str)
# print(type(json_str))





#+++++++++++.   load & dump

#  load -> str into python dis
# with open("Python/Part5/data.json", "r") as f:
#     json_is = json.load(f)
#     print(json_is)
#     print(type(json_is))


#  dump -> python dis into json str
dis = {
    "name": "Deep Kumar",
    "branch": "AIML",
    "age": 21,
    "id" : None
} 

with open("Python/Part5/data.json", "w") as f:
    json.dump(dis,f,indent=4, sort_keys=f)


