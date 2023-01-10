# 1주차 배운 내용 정리

## 바다 코끼리 연산자
```python
## 1번 코드 -> 일반 코드
s='hello world'
result = 'world' in s
if result:
    print(s)
    print(result) ## result 출력
 
 
## 2번 코드 -> := 사용
## s에 문자열을 할당하고, 'walrus' in s를 result에 할당하고, result가 True 라면
if result := 'world' in (s := 'hello world'):
    print(s)
    print(result)
```