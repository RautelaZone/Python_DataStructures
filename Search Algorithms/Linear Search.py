"""
Linear Search is also called Sequential Search
Iterative in nature
Time Complexity: O(N)
Best Time Complexity: O(1)
Worst Time Complexity: N comparisons are required
Space Complexity: O(1)

"""

l1 = [9, 1, 2, 3, 5, 7]
key = int(input("Enter the number to be searched:"))

for i in range(len(l1)):
    if key == l1[i]:
        print("Key is found at index:", i)
        break
else:
    print("Key is not found.")
