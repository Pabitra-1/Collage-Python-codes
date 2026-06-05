
n = int(input("Enter the size of array : "))

arr = []

for i in range(n):
    print(f"Enter {i + 1} th element : ", end="")
    arr.append(int(input()))

print("Array in reverse order : ", end="")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")