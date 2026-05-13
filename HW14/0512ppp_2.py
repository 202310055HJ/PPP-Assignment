import csv

def main():
    f = open("weather(146)_2001-2022.csv", "r")
    data = csv.reader(f)

    header = next(data)

    weather = []

    for row in data:
        weather.append(row)

    f.close()

    for year in range(2001, 2023):
        total_temp = 0

        for row in weather:
            y = int(row[0])
            month = int(row[1])
            tavg = float(row[4])

            if y == year:
                if month >= 5 and month <= 9:
                    total_temp = total_temp + tavg

        print(year, f"{total_temp:.1f}")


if __name__ == "__main__":
    main()
