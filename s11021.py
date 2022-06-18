T = int(input())

for i in range(T):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s" %(i+1, ans))


"""
variable을 string (문자)와 함께 출력할 때는,
연결이라는 concatenating의 기호 % 와 함께 쓴다.
쓸 곳에는 %s로 넣어 문장을 완성한 후, 
%( )안에 무엇인지 indicate 하기.

%f 실수(float)
%d 정수(integer)
%s 문자열(string)

ex)
string_1 = "eat"
string_2 = "restaurant"
print("Let's go to %s someting at the %s." %(string_1, string_2))

"""