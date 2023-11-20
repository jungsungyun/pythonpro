print("Creating a text file with the write<> method.\n")
print("Reading the newly created file.")

text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file = open("write_it.txt", "r")

print(text_file.readline())
print(text_file.readline())
print("And that would make this the third line.\n")
print("Creating a text file with the wirteline<> method.\n")
print("Reading the newly created file.")

text_file = open("write_it.txt", "a")
lines = ["That makes this line 3\n"]
text_file.writelines(lines)
text_file = open("write_it.txt", "r")
print(text_file.read())
print("\n")
print("Press the enter key to exit.")

