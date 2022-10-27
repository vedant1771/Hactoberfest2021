from itertools import permutations

lt = list()
num = int(input("Enter the range: "))
for i in range(num):
    lt.append(int(input()))
perm = permutations(lt, 4)
lt = list(perm)
count = 0
j = 0
for i in range(len(lt)):
    temp = list(lt[i])
    if temp[j] < temp[j + 1] < temp[j + 2] < temp[j + 3]:
        count = count + 1
        print(lt[i])
print(count)
