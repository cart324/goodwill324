import random
from time import sleep
money = 10000
def game(A, B):
    if A == '가위' and B == '보' or A == '바위' and B == '가위' or A == '보' and B == '바위':
        return 1
    elif A == B:
        return 2
    elif A == '가위' and B == '바위' or A == '바위' and B == '보' or A == '보' and B == '가위':
        return 3
def fo(money, bat):
    if money < bat:
        print("현제 돈보다 많이 배팅할 수 없습니다.")
        print(f"현제 돈 : {money}")
        return 0
    else:
        return 1
def slot(a, b, c):
    def sfo(two, one):
        if two == 8 or two == 15:
            return float(two ** 2)
        else:
            if one == 8 or one == 15:
                return float(two ** 2)
            else:
                return 0
    if a != b != c:
        return 0
    elif a == b and a != c:
        return sfo(a, c)
    elif a == c and a != b:
        return sfo(a, b)
    elif b == c and b != a:
        return sfo(b, a)
    elif a == b == c:
        if a == 15 or a == 8:
            print("축하합니다! 잭팟입니다!")
        return float(a * b * c)
def turn():
    tuna = random.choice(["다이아", "금", "금", "은", "은", "은", "청동", "청동", "청동", "청동", "청동", "콩", "콩", "콩", "콩", "콩", "콩", "콩", "콩", "콩"])
    if tuna == "다이아":
        return ["다이아", float(15)]
    elif tuna == "금":
        return ["금", float(8)]
    elif tuna == "은":
        return ["은", float(4)]
    elif tuna == "청동":
        return ["청동", float(2)]
    elif tuna == "콩":
        return ["콩", float(1.2)]

print("--------------------")
print("도박장에 오신걸 환영합니다.")
while True:
    true = 0
    again = 1
    if money <= 0:
        break
    print("--------------------")
    print(f"현제 돈 : {money}")
    mode = int(input("모드를 선택하세요:"))
    if mode == 1:
        print("--------------------")
        print("가위바위보에 오신걸 환영합니다.")
        while True:
            if money == 0:
                break
            true = 0
            print("--------------------")
            sleep(1)
            print(f"현제 돈 : {money}")
            again = int(input("가위바위보 1 / 나가기 2 | "))
            if again == 2:
                break
            while true == 0:
                bat = int(input("배팅할 액수를 입력하세요:"))
                true = fo(money, bat)
            money -= bat
            print("--------------------")
            A = input("무엇을 내시겟습니까?:")
            B = random.choice(["가위", "바위", "보"])
            C = game(A, B)
            if C == 1:
                money += bat * 2.5
                print("이겼습니다. 배팅액의 2.5배를 받습니다.")
            elif C == 2:
                money += bat
                print("비겼습니다. 배팅액을 돌려받습니다.")
            elif C == 3:
                print("졌습니다. 배팅액을 잃습니다.")
    elif mode == 2:
        print("--------------------")
        print("가위바위보 연승도전에 오신걸 환영합니다.")
        while True:
            if money == 0:
                break
            true = 0
            print("--------------------")
            sleep(1)
            print(f"현제 돈 : {money}")
            again = int(input("도전하기 1 / 나가기 2 | "))
            if again == 2:
                break
            gob = 0
            goa = int(input("도전할 횟수를 입력하세요:"))
            re = goa ** 2
            print(f"{goa}연승도전을 시작합니다. 승리시{re}배")
            while true == 0:
                bat = int(input("배팅할 액수를 입력하세요:"))
                true = fo(money, bat)
            money -= bat
            while gob < goa:
                gob += 1
                A = input(f"{gob}라운드 무엇을 내시겟습니까?:")
                B = random.choice(["가위", "바위", "보"])
                C = game(A, B)
                if C == 1:
                    print("이겼습니다.")
                elif C == 2:
                    gob -= 1
                    print("비겼습니다.")
                elif C == 3:
                    break
            if gob == goa:
                print(f"축하합니다! {goa}연승도전에서 승리하셨습니다!")
                print(f"배팅액의 {re}배를 받습니다!")
                money += bat * re + bat
            else:
                print(f"{goa}연승도전 {gob}라운드에서 탈락하셨습니다. 배팅액을 잃습니다.")
    elif mode == 3:
        print("--------------------")
        print("연속 가위바위보에 오신걸 환영합니다.")
        while True:
            if money == 0:
                break
            true = 0
            print("--------------------")
            sleep(1)
            print(f"현제 돈 : {money}")
            again = int(input("가위바위보 1 / 나가기 2 | "))
            if again == 2:
                break
            winc = 0
            drawc = 0
            losec = 0
            while true == 0:
                bat1 = int(input("배팅할 액수를 입력하세요:"))
                count = int(input("연속으로 진행할 횟수를 입력하세요:"))
                bat = bat1 * count
                true = fo(money, bat)
            money -= bat
            A = input("연속으로 무엇을 내시겟습니까?")
            while count > 0:
                count -= 1
                B = random.choice(["가위", "바위", "보"])
                C = game(A, B)
                if C == 1:
                    winc += 1
                elif C == 2:
                    drawc += 1
                elif C == 3:
                    losec += 1
            print(f"{winc}번 이김, {drawc}번 비김, {losec}번 짐")
            while winc > 0:
                winc -= 1
                money += bat * 2.5
            while drawc > 0:
                drawc -= 1
                money += bat
    elif mode == 4:
        print("--------------------")
        print("슬롯머신에 오신걸 환영합니다.")
        while True:
            if money == 0:
                break
            true = 0
            print("--------------------")
            sleep(1)
            print(f"현제 돈 : {money}")
            again = int(input("슬롯머신작동 1 / 나가기 2 | "))
            if again == 2:
                break
            while true == 0:
                bat = int(input("배팅할 액수를 입력하세요:"))
                true = fo(money, bat)
            money -= bat
            sa = turn()
            sb = turn()
            sc = turn()
            print("--------------------")
            sleep(1)
            print(f"{sa[0]}, {sb[0]}, {sc[0]}")
            multi = slot(sa[-1], sb[-1], sc[-1])
            if multi == 0:
                print("꽝입니다")
            else:
                print(f"{multi}배를 획득하였습니다.")
            money += bat * multi
        else:
            print("뷁")
    elif mode == 5:
        print("--------------------")
        print("블랙잭에 오신걸 환영합니다.")
        while True:
            if money == 0:
                break
            true = 0
            print("--------------------")
            sleep(1)
            print(f"현제 돈 : {money}")
            again = int(input("플레이 1 / 나가기 2 | "))
            if again == 2:
                break
            while True:
                deal = 0
                user = 0
                while true == 0:
                    bat = int(input("배팅할 액수를 입력하세요:"))
                    true = fo(money, bat)
                money -= bat
                deal1 = random.randrange(1, 14)
                deal2 = random.randrange(1, 14)
                deal3 = random.randrange(1, 14)
                deal4 = random.randrange(1, 14)
                deal5 = random.randrange(1, 14)
                user1 = random.randrange(1, 14)
                user2 = random.randrange(1, 14)
                user3 = random.randrange(1, 14)
                user4 = random.randrange(1, 14)
                user5 = random.randrange(1, 14)
                deal = deal1 + deal2
                user = user1 + user2
                print("--------------------")
                sleep(1)
                if deal == 21:
                    print(f"딜러 : {deal1}, {deal2} = {deal}")
                    print("블랙잭")
                    sleep(1)
                    print(f"유저 : {user1}, {user2} = {user}")
                    if user == 21:
                        print("블랙잭")
                        print("무승부")
                        money += bat
                        break
                    else:
                        print("패배")
                        break
                print(f"딜러 : {deal1}, ???")
                print(f"유저 : {user1}, {user2} = {user}")
                if user == 21:
                    print("블랙잭")
                    print("이겼습니다.")
                    money += bat * 2.5
                    break
                elif user > 21:
                    print("버스트")
                    print("졌습니다.")
                    break
                else:
                    hit = int(input("1:더블다운 / 2:힛 / 3:스탠드 | "))
                    if hit == 1:
                        user += user3
                        money -= bat
                        bat += bat
                        print(f"유저 : {user1}, {user2}, {user3} = {user}")
                        if user > 21:
                            print("버스트")
                            print("졌습니다.")
                            break
                        elif user == 21:
                            print("블랙잭")
                    elif hit == 2:
                        user += user3
                        print(f"유저 : {user1}, {user2}, {user3} = {user}")
                        if user > 21:
                            print("버스트")
                            print("졌습니다.")
                            break
                        elif user == 21:
                            print("유저 : 블랙잭")
                        else:
                            hit = int(input("2:힛 / 3:스탠드 | "))
                            if hit == 2:
                                user += user4
                                print(f"유저 : {user1}, {user2}, {user3}, {user4} = {user}")
                                if user > 21:
                                    print("버스트")
                                    print("졌습니다.")
                                    break
                                elif user == 21:
                                    print("블랙잭")
                                else:
                                    hit = int(input("2:힛 / 3:스탠드 | "))
                                    if hit == 2:
                                        user += user5
                                        print(f"유저 : {user1}, {user2}, {user3}, {user4}, {user5} = {user}")
                                        if user > 21:
                                            print("버스트")
                                            print("졌습니다.")
                                            break
                                        elif user == 21:
                                            print("블랙잭")
                                        else:
                                            pass
                                    elif hit == 3:
                                        pass
                                    else:
                                        print("뷁")
                                        pass
                            elif hit == 3:
                                pass
                            else:
                                print("뷁")
                                pass
                    elif hit == 3:
                        pass
                    else:
                        print("뷁")
                        pass
                    sleep(1)
                    print("딜러 턴")
                    sleep(1)
                    print(f"딜러 : {deal1}, {deal2} = {deal}")
                    if deal < 17:
                        sleep(2)
                        deal += deal3
                        print(f"딜러 : {deal1}, {deal2}, {deal3} = {deal}")
                        if deal > 21:
                            print("버스트")
                            print("이겼습니다.")
                            money += bat * 2.5
                            break
                        elif deal == 21:
                            print("블랙잭")
                        elif deal < 17:
                            sleep(2)
                            deal += deal4
                            print(f"딜러 : {deal1}, {deal2}, {deal3}, {deal4} = {deal}")
                            if deal > 21:
                                print("버스트")
                                print("이겼습니다.")
                                money += bat * 2.5
                                break
                            elif deal == 21:
                                print("블랙잭")
                            elif deal < 17:
                                sleep(2)
                                deal += deal5
                                print(f"딜러 : {deal1}, {deal2}, {deal3}, {deal4}, {deal5} = {deal}")
                                if deal > 21:
                                    print("버스트")
                                    print("이겼습니다.")
                                    money += bat * 2.5
                                    break
                                elif deal == 21:
                                    print("블랙잭")
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    sleep(2)
                    if deal == 21 and user == 21:
                        print("비겼습니다.")
                        break
                    else:
                        print(f"딜러 : {deal} / 유저 : {user}")
                        sleep(1)
                        if deal > user:
                            print("졌습니다.")
                        elif deal == user:
                            print("비겼습니다.")
                            money += bat
                        elif deal < user:
                            print("이겼습니다.")
                            money += bat * 2.5
                    break
    elif mode == 1234567890324:
        money += int(input("추가할 액수를 입력해세요:"))
    else:
        print("뷁")
sleep(1)
print("돈을 모두 잃었습니다. 게임을 종료합니다.")