def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if getDivisor(i):
            answer+=i
        else:
            answer-=i        
    return answer

def getDivisor(n):
    lst = []
    for i in range(1, n + 1):
        if (n % i == 0) :
            lst.append(i)
    if len(lst)%2 ==0:
        return True
    else:
        return False
    
    
'''
#제곱수의 약수의 개수는 홀수

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'''