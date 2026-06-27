try:
    with open("data.txt", "r") as source, open("data2.txt", "w") as target:
        target.write(source.read())

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found!")