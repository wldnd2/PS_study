# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
from heapq import heappush, heappop, heapify
def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        cnt += 1
        heappush(scoville, heappop(scoville) + heappop(scoville)*2)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))