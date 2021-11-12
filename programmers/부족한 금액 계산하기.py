def solution(price, money, count):
    answer = 0
    
    for i in range(1,count+1):
        answer+= (i*price)
    answer = money - answer
    if answer<0:
        return answer * -1
    else:
        return 0


'''

# 3,6,9,...을 수열이라 보고 등차수열의 합 공식을 구해주면 price*(count**2)+count//2 - money

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


'''