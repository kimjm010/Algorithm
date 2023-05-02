from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft
queue.append(1)
queue.append(4)
queue.popleft

print(queue)
queue.reverse()
print(queue)

def factorial_recusrive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recusrive(n - 1)

#최대 공약수 계산(유클리드 호제법) -> 두 개의 자연수에 대한 최대공약수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    