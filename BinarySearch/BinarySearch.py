l1 = [1, 2, 3, 5, 7]
l1.sort()
low = 0
high = len(l1) - 1
found = False
key = int(input("Enter the number to be searched:"))
while low <= high and not found:
    mid = (low + high) // 2
    if key == l1[mid]:
        found = True
    elif key > l1[mid]:
        low = mid + 1
    elif key < l1[mid]:
        high = mid - 1
if found:
    print(f"Key {key} found at index:", mid)
else:
    print("Key not found")
