
N,M = map(int,input().split())
print((N-1)+N*(M-1))

"""
[split chocolates]

New functions 
1. split 
    def : input으로 입력된 문자열을 나누어주는 역할 
    gram : input .split(sep, maxsplit, number)
    cf : 시분초를 input으로 받았는데 이것을 각각 떼낼 때, 나이와 출생년도를 같이 받았는데 떼넬 때
2. map
    def : 여러 요소에 한번에 일정 값을 대응해줄 수 있음. 반복작업 필요 없음
    gram : variable name = map(type, element)
    cf : 각 제품 가격을 더블로 바꿀때, 하나의 리스트에 각각 *2하여 새로운 list를 만들 때,   
         map(int,input().split())

"""