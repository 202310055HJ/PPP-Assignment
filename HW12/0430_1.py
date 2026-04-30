
def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset


def read_tmax(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[4]))
    return dataset


def get_day_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5.0:
            count_5mm += 1
    return count_5mm


def get_rain_event_5mm(rainfall):
    dataset_rainfall = []


    for r in rainfall:
        if r > 0:
            dataset_rainfall.append(1)
        else:
            dataset_rainfall.append(0)

    dataset_rain_event = []

    for i in range(len(dataset_rainfall)):
        r = dataset_rainfall[i]

        if r == 0:
            dataset_rain_event.append(0)
        else:
            if i == 0:
                dataset_rain_event.append(1)
            else:
                dataset_rain_event.append(dataset_rain_event[i-1] + 1)

    print(dataset_rain_event)
    return max(dataset_rain_event)


def get_max_rainfall_event(rainfall):
    datasets = []
    rainfall_event = None

    for r in rainfall:
        if r > 0:
            if rainfall_event != None:
                rainfall_event.append(r)
            else:
                rainfall_event = [r]
        else:
            if rainfall_event != None:
                datasets.append(rainfall_event)
                rainfall_event = None


    if rainfall_event != None:
        datasets.append(rainfall_event)

    print(datasets)
    print(max([len(x) for x in datasets]))
    return max([sum(x) for x in datasets])


def get_top3(list_values):
    return sorted(list_values)[-3:]


def main():
    weather_filename = "weather(146)_2022-2022.csv"

    rainfall = read_rainfall(weather_filename)
    print(rainfall)

    days_over_5mm = get_day_over_5mm(rainfall)
    print(f"5mm 이상인 총 강우일수는{days_over_5mm}입니다.")

    max_rainy_days = get_rain_event_5mm(rainfall)
    print(f"5mm 이상인 최장 연속 강우일수는{max_rainy_days}입니다.")

    max_rainfall_event = get_max_rainfall_event(rainfall)
    print(f"최대 강우량은{max_rainfall_event}mm입니다.")   

    tmax = read_tmax(weather_filename)
    tmax_top3 = get_top3(tmax)
    print(f"tmax 최대값 3개는 {tmax_top3}입니다")


if __name__ == "__main__":
    main()