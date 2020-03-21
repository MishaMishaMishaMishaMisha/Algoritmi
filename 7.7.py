def issort(array):
    for i in range(len(array)):
        if i != len(array) - 1 and array[i] > array[i + 1]:
            return False
    return True

def ar_to_str(array):
    s = ''
    for i in array:
        s += str(i) + ' '
    return s[:-1]


file1 = open("input77.txt", "r")
N = file1.readline()
ar = file1.readline().split()
file1.close()
array = []
for i in range(int(N)):
    array.append(int(ar[i]))

file2 = open("output77.txt", "w")
if not issort(array):
    l = len(array)
    for i in range(1, l):
        k = 0
        value = array[i]
        index = i
        while index > 0:
            if array[index - 1] > value:
                array[index] = array[index - 1]
                k += 1
            else:
                break
            index -= 1
        array[index] = value
        if k != 0:
            file2.write(ar_to_str(array) + '\n')
file2.close()

