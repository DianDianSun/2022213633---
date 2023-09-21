import numpy as np
import time
# 计算方法1
e1 = 1
i = 1
n = 100000
time_pre = time.time()
while i <= 100000:
    e1 *= 1 + 1 / n
    i += 1
time1 = time.time() - time_pre
print("第一种计算方法计算出e",e1)
print("第一种计算方法计算误差",np.abs(e1-np.e))
print("第一种计算方法计算时间",time1)
# 计算方法2
e2 = 1
i = 1
n = 1
time_pre = time.time()
while i <= 100000:
    n *= i
    e2 += 1/n
    i += 1
time2 = time.time() - time_pre
print("第二种计算方法计算出e:",e2)
print("第二种计算方法计算误差:",np.abs(e2-np.e))
print("第二种计算方法计算时间:",time2)