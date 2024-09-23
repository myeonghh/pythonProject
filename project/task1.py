import random





while True:

    chance = 0
    print("1.이지모드 : 기회 20번, 2.노말모드 : 기회 15번, 3.하드모드 : 기회 10번")

    while True:
        num = int(input("난이도를 선택 하세요 : "))

        if num == 1:
            chance = 20
        elif num == 2:
            chance = 15
        elif num == 3:
            chance = 10
        else:
            print("다시 선택 하세요")
            continue
        break

    print(f"기회 : {chance}")
    rannum_list = sorted(random.sample(range(0, 10), 3))
    print(f"랜덤 숫자 : {rannum_list}")

    win_chk = False

    for i in range(0, chance):

        while True:
            numlist = []
            num_str = input("숫자 3개를 입력하세요 : ")

            for j in range(0, len(num_str)):
                numlist.append(int(num_str[j]))

            if len(num_str) != 3:
                print("다시 입력 하세요")
                continue

            if len(numlist) != len(set(numlist)):
                print("숫자가 중복 됩니다 다시 입력하세요")
                continue

            break

        print(f"{i+1}번째 기회 : {numlist}")

        strike_cnt = 0
        ball_cnt = 0
        for j in range(0, 3):
            if numlist[j] == rannum_list[j]:
                strike_cnt += 1
                continue
            for k in range(0, 3):
                if numlist[j] == rannum_list[k]:
                    ball_cnt += 1

        if strike_cnt == 0 and ball_cnt == 0:
            print("[OUT]")
        else:
            print(f"[{strike_cnt} strike / {ball_cnt} ball]")

        if strike_cnt == 3:
            print("축하합니다 승리했습니다!!!!!!")
            win_chk = True
            break
    if win_chk == False:
        print("기회가 다 소진 되어 패배했습니다 ㅠㅠ")

    print("다시 하시 겠습니까????")
    replay_num = int(input("1. 예 2. 아니오 : "))

    if replay_num == 1:
        continue
    else:
        break













