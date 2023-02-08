# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    depth = len(numbers)
    def dfs(start, result):
        # 어느정도 깊이로 들어갔는지 확인
        if depth == start:
            # 최종 결과가 같으면 ++
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(start+1, result+numbers[start])
            dfs(start+1, result-numbers[start])
    dfs(0,0)
    return answer

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))