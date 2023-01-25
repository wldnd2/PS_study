# 위장
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    look = {}
    for item in clothes:
        try: look[item[1]].append(item[0])
        except: look[item[1]] = [item[0]]
    for value in look.values():
        answer *= (len(value) + 1)
    return answer - 1

# from collections import Counter
# from functools import reduce
# def solution(clothes):
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))