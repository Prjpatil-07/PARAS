key_list = ["Name", "Age", "Gender"]
value_list = ["Paras", 20, "Male"]

my_dict = dict(zip(key_list, value_list))
print(my_dict)

my_dict = {}

for i, ikey in enumerate(key_list):
    my_dict[ikey] = value_list[i]    

print(my_dict)

i = 0
for ikey in key_list:
    my_dict[ikey] = value_list[i]
    i += 1  

print(my_dict)