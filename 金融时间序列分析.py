# Author: melon
# CreatTime:2024/12/3
# FileName：金融时间序列分析
# Description: focus on the code
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set_style('darkgrid')

data = pd.read_csv('history_price_data.csv',index_col=0,parse_dates=True)
data.plot(figsize=(10,12))
plt.show()