def sherlock_beast(n):
    output = []
    temp = n
    i = 0
    rem = n % 3
    if rem == 0:
        while i < n:
            output.append(5)
            i += 1
    if rem == 1:
        qo = n / 3
        if qo > 2:
            while i < (qo-3)*3:
                output.append(5)
                i += 1
            while i < n:
                output.append(3)
                i += 1
        else:
            output.append(-1)
    if rem == 2:
        qo = n / 3
        while i < (qo-1)*3:
            output.append(5)
            i += 1
        while i < n and n > 3:
            output.append(3)
            i += 1
        if n < 3:
            output.append(-1)
            
    op = ''
    for each in output:
        op += str(each)

    print op

t = input()
n = []
for i in range(t):
    n.append(input())

for i in range(t):
    sherlock_beast(n[i])
