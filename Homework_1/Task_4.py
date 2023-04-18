f = open('1.txt')
n = int(f.readline())
maxlen = 0
screen = [['0'] * 10001 for i in range(10001)]
for i in f:
    x, y = i.split()
    screen[int(x)][int(y)] = '1'
for i in range(1, 10001):
    count = 0
    for j in range(1, 10001):
        if j % 2 != 0:
            if (screen[i][j] == '1') and (screen[i][j + 1] == '0'):
                count = count + 1
            else:
                if count > maxlen:
                    maxlen = count
                    maxnum = i
                count = 0
print(maxlen, maxnum)
  