# from itertools import combinations
# def solution(number, k):
#     temp = list(combinations(number, len(number) - k))
#     result = [int("".join(item)) for item in temp]
#     return str(max(result))
def solution(number, k):
    answer = []
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    return "".join(answer[:len(answer)-k])

print(solution("1924",2))
print(solution("1231234", 3))
print(solution("4177252841", 4))