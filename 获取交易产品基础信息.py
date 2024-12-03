import okx.Account as Account

# API 初始化
apikey = "088a5133-8702-4fb0-b0e4-19543a3365b0"
secretkey = "81340C0AC715345C58644C329222CECB"
passphrase = "Jimmysinktest1!"

flag = "1"  # 实盘:0 , 模拟盘:1

accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

result = accountAPI.get_instruments(instType="SPOT")
print(result)


