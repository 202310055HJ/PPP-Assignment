import csv

csv_filename = "식품의약품안전처_통합식품영양성분정보_20260604.csv"

food_db = []

with open(csv_filename, "r", encoding="utf-8") as f:
    # 'encoding="utf-8"'은 한글 깨짐 방지!

    csv_reader = csv.DictReader(f)


    for row in csv_reader:

        food_db.append(row)


# ---------------------------------------------------------------------------
# [계산식 및 기능 함수 정의]
# ---------------------------------------------------------------------------

# 기초대사량(BMR) 계산 함수
def 계산_기초대사량(gender, weight, height, age):
    if gender == "1":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161

# 활동 계수 구하는 함수
def 계산_활동계수(activity):
    if activity == "1":
        return 1.2
    elif activity == "2":
        return 1.375
    elif activity == "3":
        return 1.55
    else:
        return 1.725

# 탄단지 목표 그램수 환산 함수
def 계산_탄단지목표(kcal):
    carbo = (kcal * 0.5) / 4
    protein = (kcal * 0.2) / 4
    fat = (kcal * 0.3) / 9
    return carbo, protein, fat

# 공공데이터 빈값 처리 함수
def 빈값체크(val):
    if val == "":
        return 0.0
    else:
        return float(val)

# 음식 영양성분 계산 함수
def 계산_영양소(selected_food, eat_gram):
    weight_ratio = eat_gram / 100

    f_kcal = selected_food["에너지(kcal)"]
    f_carbo = selected_food["탄수화물(g)"]
    f_pro = selected_food["단백질(g)"]
    f_fat = selected_food["지방(g)"]

    # 값이 비어있지 않으면 실수로 비어있으면 0.0으로 처리
    kcal_val = 빈값체크(f_kcal)
    carbo_val = 빈값체크(f_carbo)
    pro_val = 빈값체크(f_pro)
    fat_val = 빈값체크(f_fat)

    cal_kcal = kcal_val * weight_ratio
    cal_carbo = carbo_val * weight_ratio
    cal_pro = pro_val * weight_ratio
    cal_fat = fat_val * weight_ratio

    # 오늘 먹은 음식 이름, 그램 수, 계산된 영양성분들
    return {
        "name": selected_food["식품명"],
        "gram": eat_gram,
        "kcal": cal_kcal,
        "carbo": cal_carbo,
        "pro": cal_pro,
        "fat": cal_fat
    }


# ---------------------------------------------------------------------------
# [메인 프로그램 함수]
# ---------------------------------------------------------------------------
def main():
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    print("=== 나만의 하루 영양성분 계산기 ===")
    print(f"로딩 완료! 음식 데이터 {len(food_db)}개!\n")


    run_program = True

    while run_program:
        #  4번(종료)을 누르기 전까지 무한 반복

        print("----- [ 1단계: 사용자 신체 정보 입력 ] -----")
        user_name = input("이름: ")
        user_gender = input("성별 (1. 남자 / 2. 여자): ")
        user_age = int(input("나이: "))
        user_height = float(input("키(cm): "))
        user_weight = float(input("몸무게(kg): "))


        print("활동량 선택 (1. 거의없음 / 2. 가벼운활동 / 3. 보통 / 4. 활동량 많음)")
        user_activity = input("번호: ")


        my_bmr = 계산_기초대사량(user_gender, user_weight, user_height, user_age)
        # 기초대사량(BMR) 남녀 공식이 살짝 달라서 다르게 계산했씀다

        act_index = 계산_활동계수(user_activity)

        limit_kcal = my_bmr * act_index
        # 하루 총 권장 칼로리


        limit_carbohydrate, limit_protein, limit_fat = 계산_탄단지목표(limit_kcal)
        #  탄수화물 50% : 단백질 20% : 지방 30%
        #  탄수화물과 단백질은 1g당 4kcal
        #  지방은 1g당 9kcal

        today_records = []

    #--ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        menu_loop = True


        while menu_loop:
            # 4번 종료 누르기 전까지 무한 재생
            print("\n================ [ 메인 메뉴 ] ================")
            print("1. 나의 하루 권장 섭취량 확인")
            print("2. 먹은 음식 검색 및 추가")
            print("3. 오늘 먹은 영양성분 총계 및 남은 칼로리 보기")
            print("4. 프로그램 완전히 종료")
            print("===============================================")

            #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            select_menu = input("원하는 메뉴 번호 입력: ")

            if select_menu == "1":

                print(f"\n[ {user_name}님의 하루 권장 섭취 가이드 ]")
                print(f"▶ 목표 칼로리: {round(limit_kcal, 1)} kcal")
                print(f"▶ 권장 탄수화물: {round(limit_carbohydrate, 1)} g")
                print(f"▶ 권장 단백질: {round(limit_protein, 1)} g")
                print(f"▶ 권장 지방: {round(limit_fat, 1)} g")

                #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            elif select_menu == "2":

                print("\n검색할 음식 키워드를 입력하세요: ") # \n로 보기 쉽게 했습니다 + 2번은 AI의 도움이 있습니다..
                search_word = input()
                search_results = []

                for food in food_db:
                    if search_word in food["식품명"]:
                        search_results.append(food)

                    if len(search_results) == 10:
                        break

                if len(search_results) == 0:
                    print("※ 검색 결과가 없습니다. 다시 검색해주세요.")

                else:
                    print(f"\n'{search_word}' 검색 결과 (상위 10개)")

                    for i in range(len(search_results)):
                        print(
                            i + 1,
                            ".",
                            search_results[i]["식품명"],
                            "-",
                            search_results[i]["에너지(kcal)"],
                            "kcal"
                        )

                    choice_num = int(input("먹은 음식의 번호를 선택하세요: "))
                    eat_gram = float(input("섭취량(g)을 입력하세요: "))

                    selected_food = search_results[choice_num - 1]


                    record_item = 계산_영양소(selected_food, eat_gram)

                    today_records.append(record_item)
                    # 누적
                    print(f" {selected_food['식품명']} ({eat_gram}g)이 추가되었습니다.")
    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            elif select_menu == "3":
                #  지금까지 먹은 것과 목표량 대비 남은 양
                sum_kcal = 0.0
                sum_carbo = 0.0
                sum_pro = 0.0
                sum_fat = 0.0
                # 합계를 구해야 하니까 일단 전부 0.0

                print("\n[ 오늘 먹은 음식 내역 ]")
                if len(today_records) == 0:
                    print("현재까지 먹은 음식이 없습니다.")
                else:
                    for item in today_records:

                        print(f"- {item['name']} {item['gram']}g -> {round(item['kcal'], 1)} kcal")
                        sum_kcal += item['kcal']
                        sum_carbo += item['carbo']
                        sum_pro += item['pro']
                        sum_fat += item['fat']
                        # 반복문으로 여태 먹은 총합

                print("\n[ 총 섭취량 VS 권장량 비교 ]")
                print(
                    f"▶ 칼로리: {round(sum_kcal, 1)} / {round(limit_kcal, 1)} kcal (남은 양: {round(limit_kcal - sum_kcal, 1)} kcal)")
                print(
                    f"▶ 탄수화물: {round(sum_carbo, 1)} / {round(limit_carbohydrate, 1)} g (남은 양: {round(limit_carbohydrate - sum_carbo, 1)} g)")
                print(
                    f"▶ 단백질: {round(sum_pro, 1)} / {round(limit_protein, 1)} g (남은 양: {round(limit_protein - sum_pro, 1)} g)")
                print(f"▶ 지방: {round(sum_fat, 1)} / {round(limit_fat, 1)} g (남은 양: {round(limit_fat - sum_fat, 1)} g)")
                #  [지금까지 먹은 것] / [하루 권장량]
                #  [권장량 - 먹은 양]으로 오늘 얼마나 더 먹어도 되는지
                #  AI의 도움이 있었습니다..

    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            elif select_menu == "4":
                print("\n 이용해 주셔서 감사합니다.")
                menu_loop = False
                run_program = False
                #  내부 반복 스위치(`menu_loop`)와 외부 프로그램 스위치(`run_program`)

            else:
                # 이상한거 쳤을 때 대비
                print("※ 잘못된 번호입니다. 1번부터 4번 사이의 숫자를 입력해주세요.")

#실행!ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
main()