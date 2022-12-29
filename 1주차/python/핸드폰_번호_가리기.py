def solution(phone_number):
    temp = list(phone_number)
    for i in range(len(temp[:-4])):
        temp[i] = "*"
    return "".join(temp)

# 다른 해답
# def solution(phone_number):
#     return "*"*(len(phone_number)-4) + phone_number[-4:]