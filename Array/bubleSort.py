
n = int(input("Enter the size of array : "))

arr = []

for i in range(n):
    print(f"Enter {i + 1} th element : ", end="")
    arr.append(int(input()))

# Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

print("[ ", end="")
for ele in arr:
    print(ele, end=" ")
print("]")