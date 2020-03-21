with open('input55.txt', 'r', encoding="Cp1252") as inputfile:
    f = inputfile.readlines()
temp = []
for i in f:
    temp.append(i)
    
word = temp[0]
N = int(temp[1])
words = []
for i in range(2, N + 2):
    words.append(temp[i])

def kal_bukv(s, b):
    k = 0
    for i in range(len(s)):
        if s[i] == b:
            k += 1
    return k

for wrds in words:
    for j in range(len(wrds)):
        if kal_bukv(wrds, wrds[j]) > kal_bukv(word, wrds[j]):
            N -= 1
            break

file1 = open("output55.txt", "w")
file1.write(str(N))
file1.close()
