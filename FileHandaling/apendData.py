text = input("Enter text: ")

with open("data.txt", "a") as file:
    file.write("\n" + text + "\n")

print("Data appended successfully")