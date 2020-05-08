import random
money = 10000
def game(A, B):
    if A == '가위' and B == '보' or A == '바위' and B == '가위' or A == '보' and B == '바위':
        return 1
    elif A == B:
        return 2
    elif A == '가위' and B == '바위' or A == '바위' and B == '보' or A == '보' and B == '가위':
        return 3
def win(money, bat):
    return round(bat * 2.5 + money)
def draw(money, bat):
    return round(money + bat)
def fo(money, bat):
    if money < bat:
        print("현제 돈보다 많이 배팅할 수 없습니다.")
        print(f"현제 돈 : {money}")
        return 0
    else:
        return 1

while True:
    true = 0
    print(f"현제 돈 : {money}")
    if money <= 0:
        break
    mode = int(input("모드를 선택하세요:"))
    if mode == 1:
        while true == 0:
            bat = int(input("배팅할 액수를 입력하세요:"))
            true = fo(money, bat)
        money = money - bat
        A = input("무엇을 내시겟습니까?:")
        B = random.choice(["가위", "바위", "보"])
        C = game(A, B)
        if C == 1:
            money = win(money, bat)
            print("이겼습니다. 배팅액의 2.5배를 받습니다.")
        elif C == 2:
            money = draw(money, bat)
            print("비겼습니다. 배팅액을 돌려받습니다.")
        elif C == 3:
            print("졌습니다. 배팅액을 잃습니다.")
    elif mode == 2:
        gob = 0
        goa = int(input("도전할 횟수를 입력하세요:"))
        re = goa ** 2
        print(f"{goa}연승도전을 시작합니다. 승리시{re}배")
        while true == 0:
            bat = int(input("배팅할 액수를 입력하세요:"))
            true = fo(money, bat)
        money = money - bat
        while gob < goa:
            gob = gob + 1
            A = input(f"{gob}라운드 무엇을 내시겟습니까?:")
            B = random.choice(["가위", "바위", "보"])
            C = game(A, B)
            if C == 1:
                print("이겼습니다.")
            elif C == 2:
                gob = gob - 1
                print("비겼습니다.")
            elif C == 3:
                break
        if gob == goa:
            print(f"축하합니다! {goa}연승도전에서 승리하셨습니다!")
            print(f"배팅액의 {re}배를 받습니다!")
            money = bat * re + money
        else:
            print(f"{goa}연승도전 {gob}라운드에서 탈락하셨습니다. 배팅액을 잃습니다.")
    elif mode == 3:
        winc = 0
        drawc = 0
        losec = 0
        while true == 0:
            bat1 = int(input("배팅할 액수를 입력하세요:"))
            count = int(input("연속으로 진행할 횟수를 입력하세요:"))
            bat = bat1 * count
            true = fo(money, bat)
        money = money - bat
        bat = bat1
        A = input("연속으로 무엇을 내시겟습니까?")
        while count > 0:
            count = count - 1
            B = random.choice(["가위", "바위", "보"])
            C = game(A, B)
            if C == 1:
                winc = winc + 1
            elif C == 2:
                drawc = drawc + 1
            elif C == 3:
                losec = losec + 1
        print(f"{winc}번 이김, {drawc}번 비김, {losec}번 짐")
        while winc > 0:
            winc = winc - 1
            money = win(money, bat)
        while drawc > 0:
            drawc = drawc - 1
            money = draw(money, bat)
    elif mode == 1234567890324:
        money = money + int(input("추가할 액수를 입력해세요:"))
    else:
        print("뷁")
print("돈을 모두 잃었습니다. 게임을 종료합니다.")