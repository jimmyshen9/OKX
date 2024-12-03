# Author: melon
# CreatTime:2024/12/2
# FileName：oklink-查看支持的链
# Description: focus on the code
import requests
import pandas as pd
url = "https://www.oklink.com/api/v5/explorer/tokenprice/chain-list"

payload = {

}
headers = {
  # apiKey
  'Ok-Access-Key': '761236f0-734c-4e46-90dd-9dcb8482100a'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
  data = response.json()
else:
  print("API请求失败:",response.status_code)
  data = {}
chain_list = data.get(('data'),[])

if chain_list:
  df = pd.DataFrame(chain_list)
else:
  df = pd.DataFrame()
print(df.head())

def save_to_excel(df,filename="chain_list.xlsx"):
  df.to_excel(filename,index=False)

if not df.empty:
  save_to_excel(df)
  print("数据已经保存到chain_list.xlsx文件")
else:
  print('没有数据保存')