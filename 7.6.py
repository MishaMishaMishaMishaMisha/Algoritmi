def sravnitb_slova(slovo1, slovo2):
    if len(slovo1) <= len(slovo2):
        for i in range(len(slovo1)):
            if ord(slovo1[i]) < ord(slovo2[i]):
                return slovo1
            elif ord(slovo1[i]) == ord(slovo2[i]) and i == len(slovo1) - 1:
                return slovo1
            elif ord(slovo1[i]) > ord(slovo2[i]):
                return slovo2
    else:
        for i in range(len(slovo2)):
            if ord(slovo1[i]) < ord(slovo2[i]):
                return slovo1
            elif ord(slovo1[i]) == ord(slovo2[i]) and i == len(slovo2) - 1:
                return slovo1
            elif ord(slovo1[i]) > ord(slovo2[i]):
                return slovo2

                                          
def sort_slova(array):
    l = len(array)
    for i in range(1, l):
        value = array[i]
        index = i
        while index > 0:
            if sravnitb_slova(array[index - 1], value) == value:
                array[index] = array[index - 1]
            else:
                break
            index -= 1
        array[index] = value
    return array


n = int(input())
slova = []
for i in range(n):
    slova.append(input())
sort = sort_slova(slova)
for i in sort:
    print(i)

