mart = {"우유": 2800,
        "계란": 300,
        "빵": 1200,
        "물": 1700}

cart = ["계란", "빵"]

total_cost = 0

for item in cart:
    total_cost += mart[item]

print(f"총 {total_cost}원입니다.")