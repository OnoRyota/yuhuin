import pandas #pandasをインポート
import pprint

import requests
from bs4 import BeautifulSoup

#取得したいページのurlを入力(url)
url = 'http://www.jma.go.jp/jp/amedas_h/today-83201.html'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url)

#to_json関数で文字列をjsonに変換し，OitaAmeme.jsonで保存
fetched_daraframes[4].to_json('YuhuinNoAme.json',force_ascii=False)

#プリントしたい場合
#ret = fetched_daraframes[4].to_json(force_ascii=False)
#pprint.pprint(ret)

#日付取得
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
date = soup.find(class_ = "td_title height2").get_text()
date = date + "の気象情報"

#日付をテキストファイル(date.txt)に出力
file = open('date.txt','w')
file.write(date)
file.close()
