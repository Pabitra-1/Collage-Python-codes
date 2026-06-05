
n = int(input("Enter the size of array : "))

arr = []

for i in range(n):
    print(f"Enter {i + 1} th element : ", end="")
    arr.append(int(input()))

target = 3
flag = False

for i in range(n):
    if arr[i] == target:
        print(f"Item found at index {i}")
        flag = True

if not flag:
    print("Item not found")