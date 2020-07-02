import random

money = 10000


def slot(sa, sb, sc):
    if sa != sb != sc:
        return 0
    if sa == sb != sc:
        return sa * sb
    if sa == sc != sb:
        return sa * sc
    if sb == sc != sb:
        return sb * sc
    if sa == sb == sc:
        if sa == 50 or sa == 10:
            print("축하합니다! 잭팟입니다!")
        return sa * sb * sc


def turn():
    tuna = random.choice(
        ["다이아", "클로버", "클로버", "금", "금", "금", "은", "은", "은", "은", "은", "콩", "콩", "콩", "콩", "꽝", "꽝", "꽝", "꽝", "꽝"])
    if tuna == "다이아":
        return ["다이아", 30]
    elif tuna == "클로버":
        return ["클로버", 15]
    elif tuna == "금":
        return ["금", 5]
    elif tuna == "은":
        return ["은", 3]
    elif tuna == "콩":
        return ["콩", 1.2]
    elif tuna == "꽝":
        return ["꽝", 0]


def fo(money, bat):
    if money < bat:
        print("현제 돈보다 많이 배팅할 수 없습니다.")
        print(f"현제 돈 : {money}")
        return 0
    else:
        return 1


while True:
    true = 0
    if money <= 0:
        break
    print(f"현제 돈 : {money}")
    mode = int(input("모드를 선택하세요: "))
    if mode == 4:
        print("슬롯머신에 오신걸 환영합니다.")
        while True:
            if money <= 0:
                break
            print(f"현제 돈 : {money}")
            slot_inputed = int(input("슬롯머신작동 1 / 나가기 2: "))
            if slot_inputed == 1:
                global bat
                while true == 0:
                    bat = int(input("배팅할 액수를 입력하세요: "))
                    true = fo(money, bat)
                money -= bat
                sa = turn()
                sb = turn()
                sc = turn()
                print(f"{sa[0]}, {sb[0]}, {sc[0]}")
                multi = slot(sa[-1], sb[-1], sc[-1])
                if multi == 0:
                    print("꽝입니다")
                else:
                    print(f"{multi}배를 획득하였습니다.")
                money += bat * multi
            elif slot_inputed == 2:
                break
            else:
                print("뷁")
    else:
        print("뷁")
