print("과제 6번 문제입니다 칼로리 구하기")

hallabong=int(input("한라봉의 g를 입력하세요:"))
strawberry= int(input("딸기의 g을 입력하세요:"))
banana= int(input("바나나의 g를 입력하세요:"))

hallabong_car=50/100*hallabong
strawberry_car=34/100*strawberry
banana_car=77/100*banana

print("한라봉 칼로리:",hallabong_car,"kcal")
print("딸기 칼로리", strawberry_car,"kcal")
print("바나나 칼로리",banana_car,"kcal")
print("총 섭취 칼로리",hallabong_car+strawberry_car+banana_car+banana_car,"kcal")