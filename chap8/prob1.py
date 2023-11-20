text_file = open("read_it.txt", "r")
print("Opening and closing the file.\n")
print("Reading characters from the file.")
print(text_file.read(1))
print(text_file.read(5))
print("\n")
print("Reading the entire file at once.")

text_file = open("read_it.txt","r")
whole_thing = text_file.read()
print(whole_thing)
print("Reading characters from a line.")

text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
print("Reading one line at a time.")

text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())

print("Reading the entire file into a list.")
text_file = open("read_it.txt","r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)

print("Looping through the file, line by line.")
text_file = open("read_it.txt","r")
for line in text_file:
    print(line)

print("press the enter key to exit.")
