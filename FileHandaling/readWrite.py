# Open the file in append mode
with open("data.txt", "a") as file:
    text = input("Enter string: ")
    file.write(text)

# Open the file in read mode
with open("data.txt", "r") as file:
    content = file.readline()

print(content)