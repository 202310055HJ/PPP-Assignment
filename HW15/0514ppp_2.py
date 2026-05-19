import os
import urllib.request

def download_weather_file(weather_filename):
    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"

    if os.path.exists(weather_filename):
        return

    urllib.request.urlretrieve(url, weather_filename)


def read_weather_col(weather_filename, col_idx):
    values = []

    with open(weather_filename) as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)

    return values


def main():
    weather_filename = "weather(146)_2023-2023.csv"

    download_weather_file(weather_filename)

    rainfalls = read_weather_col(weather_filename, 9)

    count = 0

    for rain in rainfalls:
        if rain >= 5:
            count = count + 1

    with open("result_rainy_days.txt", "w") as f:
        f.write(f"2023년 5mm 이상 강우일수는 {count}일입니다.")


if __name__ == "__main__":
    main()