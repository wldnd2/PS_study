def solution(citations):
    citations.sort()
    total = len(citations)
    for i in range(total):
        # h번 이상 인용된 논문이 h편 이상이라는 조건을 그대로 풀어쓴 것
        if (total - i) <= citations[i]:
            return total - i
    return 0