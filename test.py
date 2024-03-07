print("Hello world!")

variable = 21
name = "Kory"
last_name = "Plotts"
total = 07.93
age = 31
found = True

if age < 100:
    print("dont worry be happy")
elif age == 100:
    print("congrats your a century")
else:
    print("sorry, seems that you're too old!")

# Define functions
def say_hello():
    print("Hello there")

def say_goodbye(name):
    print("Goodbye " + name)

# Call the functions
say_hello()
say_goodbye("Johnny")

print("Hello my name is " + name + " and i am "+ str(age)+" years old")

#array
#list
colorList= ["white", "red", "black", "blue"] 
numberList= [1,2,3,]

#add 
colorList.append("pink")

#travel the list
for temp in colorList:
    print(temp)

#dictionary 
me={
    "first_name": "Kory",
    "last_name": "Plotts",
    "age":31
}

print(me ["first_name"])

me["age"] = 99
me ["color"]= "Blue"
print(me)