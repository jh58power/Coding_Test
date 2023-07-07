import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    input = int(sys.stdin.readline())
    arr.append(input)
    
arr.sort()

result = []
for i in arr:
    cnt = 0
    for j in range(5):
        if (i + j) not in arr:
            cnt += 1
    result.append(cnt)
    
print(min(result))