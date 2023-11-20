print("Input your string...")



text_file = open("string_it.txt", "w")

while(True):
    a = input(">> ")
    if(a == "python programming"):
        text_file.write("python programming\n")
    elif(a == "I love python"):    
        text_file.write("I love python\n")
    elif(a == "I love professor"):
        text_file.write("I love professor\n")
    elif(a == "I love programming"):
        text_file.write("I love programming\n")
    elif(a == "Q"):
        break
print("write process has been finished")
print("\n\n")

print("Your inputs are below..")
text_file = open("string_it.txt", "r")
print(text_file.read())
