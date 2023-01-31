# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 투 포인터를 이용
def solution(people, limit):
    ptr1 = 0
    ptr2 = len(people)-1
    people.sort()
    cnt = 0
    while ptr1 <= ptr2:
        cnt += 1
        if people[ptr1] + people[ptr2] <= limit:
            ptr1 += 1
        ptr2 -= 1
    return cnt