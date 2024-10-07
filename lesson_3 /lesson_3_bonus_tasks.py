def solution(x):
    p1 = x // 100
    p2 = (x // 10) % 10
    p3 = x % 10
    value = (p3 * 100) + (p2 * 10) + p1

    return value

print(solution(123))
print(solution(100))
print(solution(257))
print(solution(888))
