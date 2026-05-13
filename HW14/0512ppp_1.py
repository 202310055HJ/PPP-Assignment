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
        max_date = ""
        max_range = 0

        for row in weather:
            y = int(row[0])
            month = int(row[1])
            day = int(row[2])

            tmax = float(row[3])
            tmin = float(row[5])

            if y == year:
                temp_range = tmax - tmin

                if temp_range > max_range:
                    max_range = temp_range
                    max_date = str(year) + "." + str(month) + "." + str(day)

        print(year, max_date, f"{max_range:.1f}")


if __name__ == "__main__":
    main()
