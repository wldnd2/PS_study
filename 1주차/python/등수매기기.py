def solution(score):
    avg = [sum(item)/2 for item in score]
    return [sorted(avg, reverse=True).index(i)+1 for i in avg]

# 3시간 동안 풀었는데 //가 아니라 /여서 testcase3, 6 통과를 못했다...
# 평균은 /로 하는거 꼭! 기억하자

# :=을 사용하여 만든 다른 코드
def solution(score):
    temp = sorted((avg := [sum(item)/2 for item in score]), reverse=True)
    return [temp.index(i)+1 for i in avg]