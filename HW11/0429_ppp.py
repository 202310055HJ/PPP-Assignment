def main():
    file_name = "weather(146)_2022-2022.csv"

    tavg_list = []
    rainfall_list = []
    rainy_days_count = 0

    with open(file_name, "r", encoding="utf-8") as f:
        header = f.readline()

        for line in f:
            data = line.strip().split(",")

            tavg = float(data[4])
            rainfall = float(data[9])

            tavg_list.append(tavg)
            rainfall_list.append(rainfall)


            if rainfall >= 5.0:
                rainy_days_count += 1


    yearly_avg_temp = sum(tavg_list) / len(tavg_list)
    total_rainfall = sum(rainfall_list)

    
    print("1. 연 평균 기온: {:.2f}도".format(yearly_avg_temp))
    print("2. 5mm 이상 강우일수: {}일".format(rainy_days_count))
    print("3. 총 강우량: {:.1f}mm".format(total_rainfall))


if __name__ == "__main__":
    main()