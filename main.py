import pandas as pd
import matplotlib.pyplot as plt
import pathlib,openpyxl
from openpyxl.drawing.image import Image

file_path = pathlib.Path(__file__).parent / 'csv'
output = pathlib.Path(__file__).parent / 'result_data'
output.mkdir(parents=True, exist_ok=True)

plt.rcParams['font.family'] = 'Yu Gothic' 

df_weather = pd.read_csv(file_path / 'data_weather.csv',encoding="shift_jis",skiprows=3)
df_rain = pd.read_csv(file_path /'data_rain.csv',encoding="shift_jis",skiprows=3)

df = df_weather.merge(df_rain, on='年月日')

df['年月日'] = pd.to_datetime(df['年月日'])

year = df.groupby(df['年月日'].dt.to_period('Y')).agg({
    '平均気温(℃)': 'mean',
    '降水量の合計(mm)': 'sum'
}).reset_index()

year = year.round(1)
year['年月日'] = year['年月日'].astype(str)

fig, ax1 = plt.subplots(1,1,figsize=(10,6))
ax2 = ax1.twinx()
ax1.bar(year['年月日'],year["降水量の合計(mm)"],color="lightblue",label="年間降水量")
ax2.plot(year['年月日'],year['平均気温(℃)'],linestyle="solid",color="k",marker="o",label="平均気温(℃)")
ax1.set_title("福岡市 過去10年間の平均気温と年間降水量の推移", fontsize=16)
ax1.set_ylabel("年間降水量 (mm)", fontsize=12)
ax2.set_ylabel("平均気温 (℃)", fontsize=12)

handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1+handler2,label1+label2,borderaxespad=0)
ax1.grid(True)
plt.savefig(output /'result_data.png')


temp_trend = year['平均気温(℃)'].iloc[-1] - year['平均気温(℃)'].iloc[0]
rain_trend = year['降水量の合計(mm)'].iloc[-1] - year['降水量の合計(mm)'].iloc[0]

print(f"平均気温は過去10年で {temp_trend:.1f}℃ の変化")
print(f"年間降水量は過去10年で {rain_trend:.1f}mm の変化")

book = openpyxl.Workbook()
ws = book.active

img = Image(output / "result_data.png")
ws.title = 'result'
ws.add_image(img, "B2")

book.save(output / 'result.xlsx')