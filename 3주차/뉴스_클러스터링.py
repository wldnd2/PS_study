# https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = []
    str2_set = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_set.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_set.append(str2[i:i+2])
    intersections = Counter(str1_set) & Counter(str2_set)
    union = Counter(str1_set) | Counter(str2_set)
    try:
        answer = sum(intersections.values()) / len(list(union.elements()))
    except:
        answer = 1
    return int(answer*65536)