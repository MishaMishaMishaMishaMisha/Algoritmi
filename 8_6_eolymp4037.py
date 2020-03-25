import random
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q1 = random.randint(0, len(nums) - 1)
       q = nums[q1][0]
   l_nums = [n for n in nums if n[0] < q]
   e_nums = [n for n in nums if n[0] == q]
   r_nums = [n for n in nums if n[0] > q]
   return quicksort(l_nums) + e_nums + quicksort(r_nums)

file = open("input86.txt", "r")
N = int(file.readline())
ar = []
for i in file:
    s = i.split()
    ar.append([int(s[0]), int(s[1])])
file.close()

vs = quicksort(ar)
file1 = open("output86.txt", "w")
for i in vs:
    file1.write(str(i[0]) + ' ' + str(i[1]) + '\n')
file1.close()
