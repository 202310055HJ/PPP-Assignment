import csv

def read_weather_col(filename, col=9, data_type=float):
    result = []

    f = open(filename, "r")
    data = csv.reader(f)

    header = next(data)

    for row in data:
        result.append(data_type(row[col]))

    f.close()
    return result


def sumifs(values, conditions, criteria):
    total = 0

    for i in range(len(values)):
        if conditions[i] == criteria:
            total = total + values[i]

    return total


def main():
    weather_filename = "weather(146)_2001-2022.csv"

    rainfalls = read_weather_col(weather_filename)
    years = read_weather_col(weather_filename, 0, int)

    rainfall_2021 = sumifs(rainfalls, years, 2021)
    rainfall_2022 = sumifs(rainfalls, years, 2022)

    print(f"2021년 강수량은 {rainfall_2021:.1f}mm입니다.")
    print(f"2022년 강수량은 {rainfall_2022:.1f}mm입니다.")


if __name__ == "__main__":
    main()
