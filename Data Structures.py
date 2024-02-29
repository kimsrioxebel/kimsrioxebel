# data structure
my_list=["toyota" , "bmw" , "range" , "nissan"]
my_list.append("Mazda")
print(my_list)
print(my_list[0])
# this_list[1]="Mercedes" mutable
print(f"{my_list[1]} is manufactured in Germany")
print(type(my_list))

this_list=["4" , "6" , "9" , "8" , "6"]
this_list.insert(4, "orange")
print(this_list)

# tuple data structure
my_tuple=(  "Oranges" , "Apple" , "watermelon" , "Mangoes")
print(my_tuple)
print(f"{my_tuple[0]} I like eating Bananas")
print(my_tuple[1])
# my_tuple[1="apple"]

# Set data structure
my_set={"orange" , "yellow" , "pink" , "black" , "aqua"}
print(my_set)

# Dictionary data structure
my_dictionary={"name": "clara", "Age": 27, "Gender": "female", "year" : "2024"}
print(my_dictionary)
print(my_dictionary["Age"])
print(f"{my_dictionary['name']} my name is clara")
print(f"{my_dictionary['Gender']} am a female")
print(f"{my_dictionary['Age']} am 27 years old")