
import random


#번호 자동생성기
def Gen_num(n): 
    numbers = random.sample(range(1,46),n)
    return numbers


#당첨번호 생성기
def Gen_winningnum():
    winningnum = Gen_num(7)
    return sorted(winningnum[:6]) + winningnum[6:]

#응모번호와 당첨번호 비교
def matchingnum_cnt(numbers, winningnum):
    cnt = 0
    for num in numbers:
        if num in winningnum:
            cnt = cnt + 1
    return cnt

#확인과정
def check(numbers, winningnum):
    cnt = matchingnum_cnt(numbers, winningnum[:6])
    bonus_cnt = matchingnum_cnt(numbers, winningnum[6:])

    if cnt == 6:
        print("축하드립니다. 1등 당첨되었습니다")
        print("수령액은 1000000000원 입니다")
    elif cnt == 5 and bonus_cnt == 1:
        print("축하드립니다. 2등 당첨되었습니다")
        print("수령액은 50000000원 입니다")
    elif cnt == 5:
        print("축하드립니다. 3등 당첨되었습니다")
        print("수령액은 1000000원 입니다")
    elif cnt == 4:
        print("축하드립니다. 4등 당첨되었습니다")
        print("수령액은 50000원 입니다")
    elif cnt == 3:
        print("축하드립니다. 5등 당첨되었습니다")
        print("수령액은 5000원 입니다")
    else:
        print("꽝입니다")
        return 0


#실행부분
print("="*24)
print("로또 시뮬레이션 프로그램")
print("="*24)

numbers = []
winningnum = []

selectnum = int(input("1. 번호 직접선택    2. 번호 자동생성기 이용: "))

if(selectnum == 1):
    a, b, c, d, e, f = map(int, input("번호 6개를 입력하세요: ").split())
    numbers.append(a)
    numbers.append(b)
    numbers.append(c)
    numbers.append(d)
    numbers.append(e)
    numbers.append(f)
    print("고객님의 로또번호는 {}입니다".format(numbers))

    winningnum = Gen_winningnum()
    print("이번 당첨번호는 {} + {}입니다".format(winningnum[:6], winningnum[6:]))
    
    check(numbers, winningnum)


elif(selectnum == 2):

    numbers = Gen_num(6)
    print("고객님의 로또번호는 {}입니다".format(numbers))

    winningnum = Gen_winningnum()
    print("이번 당첨번호는 {} + {}입니다".format(winningnum[:6], winningnum[6:]))

    check(numbers, winningnum)

