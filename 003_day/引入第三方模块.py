import statistics

from statistics import median

import akshare          # 第三方库  pip install akshare

arr = [1,2,3,4,5]

mid = median(arr)
print(mid)


crypto_js_spot_df = akshare.crypto_js_spot()        # 加密货币数据  https://akshare.akfamily.xyz/data/dc/dc.html
print(crypto_js_spot_df)
