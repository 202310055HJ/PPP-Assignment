A_class = [
"김민수", "이서연", "박지훈", "최유진", "정하준",
"김민수",  # 중복
"한지민", "윤도현", "이서연"  # 중복
]
B_class = [
"박지훈", "최유진", "강다은", "오세훈", "윤도현",
"강다은",  # 중복
"김민수", "배수지"
]
print(A_class)
print(set(A_class))
print(set(B_class))
print(set(A_class) - set(B_class))
print(set(A_class) | set(B_class))
print(set(A_class) & set(B_class))