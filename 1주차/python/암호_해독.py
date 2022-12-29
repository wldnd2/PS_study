def solution(cipher, code):
    return "".join([cipher[i] for i in range(code-1, len(cipher), code)])

# 다른 해답
# def solution(cipher, code):
#     return cipher[code-1::code]