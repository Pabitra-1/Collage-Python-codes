
n = int(input("Enter the size of array : "))

arr = []

for i in range(n):
    print(f"Enter {i + 1} th element : ", end="")
    arr.append(int(input()))

target = 3

for ele in arr:
    if target == ele:
        print("Item found")
        break
else:
    print("Item not found")