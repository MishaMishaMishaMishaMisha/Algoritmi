def sort_bulb(array):
    l = len(array)
    k = 0
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                k += 1
    return k

n = int(input())
ar = input().split()
array = []
for i in range(n):
    array.append(float(ar[i]))

print(sort_bulb(array))
