def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for info in db:
        if id_pw[0] == info[0]:
            return "wrong pw"
    return "fail"

# 다른 해답
# def solution(id_pw, db):
#     if db_pw := dict(db).get(id_pw[0]):
#         return "login" if db_pw == id_pw[1] else "wrong pw"
#     return "fail"

# := 바다 코끼리 연산자
# :=는 이름을 부여하고 재사용할 수 있게 하는 것이 목적이다.
# a = [1, 2, 3, 4]
# if (n := len(a)) > 5:
#     print(f"List is too long ({n} elements, expected <= 5)")
# 이렇게 쓰면 n을 재사용할 수 있다.