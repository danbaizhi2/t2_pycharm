import time
# 获取当前时间的时间戳（秒）
timestamp = time.time()
print(timestamp)


from datetime import datetime
# 获取当前日期和时间
now = datetime.now()
# 转换为时间戳（秒）
timestamp = now.timestamp()
print(timestamp)