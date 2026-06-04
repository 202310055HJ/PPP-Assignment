import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def main():
    df_jj = pd.read_csv("weather(146)_1980-2024.csv", skipinitialspace=True)
    df_sw = pd.read_csv("weather(119)_1980-2024.csv", skipinitialspace=True)

    # 1) 전주시(146)의 2012년 연 강수량
    rain_2012 = df_jj[df_jj["year"] == 2012]["rainfall"].sum()
    print("1) 전주시 2012년 연 강수량 :", round(rain_2012, 1), "mm")

    # 2) 전주시(146)의 2024년 최대기온
    max_tmax_2024 = df_jj[df_jj["year"] == 2024]["tmax"].max()
    print("2) 전주시 2024년 최대기온 :", round(max_tmax_2024, 1), "도")

    # 3) 전주시(146)의 2020년 최대 일교차
    df_jj["tdiff"] = df_jj["tmax"] - df_jj["tmin"]
    max_tdiff_2020 = df_jj[df_jj["year"] == 2020]["tdiff"].max()
    print("3) 전주시 2020년 최대 일교차 :", round(max_tdiff_2020, 1), "도")

    # 4) 수원시(119)와 전주시(146)의 2019년 총강수량 차이
    rain_jj_2019 = df_jj[df_jj["year"] == 2019]["rainfall"].sum()
    rain_sw_2019 = df_sw[df_sw["year"] == 2019]["rainfall"].sum()
    diff = abs(rain_jj_2019 - rain_sw_2019)
    print("4) 2019년 수원시와 전주시 총강수량 차이 :", round(diff, 1), "mm")

    # 5) 1980년부터 2024년까지 전주시, 수원시 평균 기온 선그래프
    jj_temp = df_jj.groupby("year")["tavg"].mean()
    sw_temp = df_sw.groupby("year")["tavg"].mean()

    plt.plot(jj_temp.index, jj_temp, label="전주")
    plt.plot(sw_temp.index, sw_temp, label="수원")
    plt.xlabel("연도")
    plt.ylabel("평균 기온")
    plt.legend()
    plt.savefig("avg_temp_line.png")
    plt.clf()

    # 6) 1980년부터 2024년까지 전주시 연간 강수량 막대그래프
    jj_rain = df_jj.groupby("year")["rainfall"].sum()

    plt.bar(jj_rain.index, jj_rain)
    plt.xlabel("연도")
    plt.ylabel("연간 강수량")
    plt.savefig("jeonju_rain_bar.png")
    plt.clf()

    # 7) 생일 기준 온도 선그래프와 순위
    birth_year = int(input("태어난 해를 입력하시오 : "))
    month = int(input("생일 월을 입력하시오 : "))
    day = int(input("생일 일을 입력하시오 : "))

    df_day = df_jj[(df_jj["month"] == month) & (df_jj["day"] == day)]
    df_day = df_day[(df_day["year"] >= 1980) & (df_day["year"] <= 2014)]

    plt.plot(df_day["year"], df_day["tavg"])
    plt.xlabel("연도")
    plt.ylabel("평균 기온")
    plt.savefig("birthday_temp_line.png")
    plt.clf()

    sorted_df = df_day.sort_values("tavg", ascending=False)

    years = list(sorted_df["year"])

    rank = years.index(birth_year) + 1

    print("7) 내가 태어난 해는", rank, "번째로 온도가 높았습니다.")
    print("가장 온도가 높았던 해는", years[0], "년입니다.")
    print("가장 온도가 낮았던 해는", years[-1], "년입니다.")


if __name__ == "__main__":
    main()