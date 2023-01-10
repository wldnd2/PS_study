# 등차 수열의 합 공식 사용
def solution(num, total):
    return [int(((((total/num)*2)-(num-1))//2)+i) for i in range(num)]

print(solution(3,12))
print(solution(5,15))
print(solution(4,14))
print(solution(5,5))