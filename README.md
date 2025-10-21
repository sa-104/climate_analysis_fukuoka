# 福岡市 過去10年間の気候分析

## 概要
気象庁の観測データをもとに、**福岡市の過去10年間における「平均気温」と「年間降水量」の推移**を分析しました。  
気温の上昇傾向や降水量の変化をグラフで可視化し、気候変動の傾向を確認します。

---

## 使用技術
- Python 3.x  
- pandas  
- matplotlib  
- openpyxl  
- pathlib  

---

## ディレクトリ構成
climate_analysis_fukuoka/
│
├─ csv/ # CSVデータを格納
│ ├─ data_weather.csv # 気温データ
│ └─ data_rain.csv # 降水量データ
│
├─ result_data/ # 結果出力フォルダ
│ ├─ result_data.png # グラフ画像
│ └─ result.xlsx # グラフを貼り付けたExcelファイル
│
├─ main.py # 実行スクリプト
└─ README.md # この説明ファイル


##  実行方法

### 1. リポジトリをクローンまたはダウンロード
```bash
git clone https://github.com/<sa-104>/climate_analysis_fukuoka.git

pip install pandas matplotlib openpyxl
3. CSVデータを配置
csv フォルダ内に以下の2ファイルを置いてください：

data_weather.csv

data_rain.csv

（※気象庁サイトなどから取得）

4. 実行
bash
コードをコピーする
python main.py

 出力結果
result_data.png
→ 年ごとの平均気温と年間降水量の二軸グラフ

result.xlsx
→ 上記グラフを貼り付けたExcelファイル

分析結果（例）
コードをコピーする
平均気温は過去10年で +0.8℃ の変化
年間降水量は過去10年で +120mm の変化

学習・実装ポイント
pandasでのデータ前処理（欠損処理・結合・集計）

matplotlibでの二軸グラフ作成

openpyxlでのExcelファイル出力と画像貼り付け

pathlibを用いた柔軟なパス管理

今後の発展案

他都市（東京・大阪など）との比較

月ごとの平均推移グラフ化

Webアプリ化（Streamlitなどで可視化）