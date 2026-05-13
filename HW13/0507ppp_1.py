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


def main():
    weather_filename = "weather(146)_2022-2022.csv"

    rainfalls = read_weather_col(weather_filename)

    print(f"2022년 총 강수량은 {sum(rainfalls):.1f}mm입니다.")


if __name__ == "__main__":
    main()
