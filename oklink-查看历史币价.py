# Author: melon
# CreatTime:2024/12/2
# FileName：oklink-查看历史币价
# Description: focus on the code
import requests
from datetime import datetime,timedelta
import pandas as pd
url = "https://www.oklink.com/api/v5/explorer/tokenprice/historical"

payload = {
  'chainId': '0',
  'limit': '200',
  'period':'1D'
}
headers = {
  # apiKey
  'Ok-Access-Key': '761236f0-734c-4e46-90dd-9dcb8482100a'
}

all_data = []
last_timestamp = None
num_requests = 10

for i in range(num_requests):
  if last_timestamp:
    payload['after'] = last_timestamp  # 获取此时间戳之前的数据
  response = requests.request("GET", url, headers=headers,params=payload)
  data = response.json()

  price_data = data.get("data",[])

  data_list = []
  for entry in price_data:
    timestamp = entry.get("time")
    price = entry.get("price")

    if timestamp and price:
      timestamp = int(timestamp)
      date = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
      data_list.append([date,price])
  all_data.extend(data_list)

  last_timestamp = price_data[-1].get("time")

df = pd.DataFrame(all_data,columns=['Date','Price'])
df.to_csv("history_price_data.csv",index=False)
print("成功写入")
