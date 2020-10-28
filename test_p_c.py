import  main_Quantification_02
import numpy as np
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

plane_in = "D:/workspace/python/test/01_实证网络_train_car_plane/data/plane_in.csv"
train_in = "D:/workspace/python/test/01_实证网络_train_car_plane/data/train_in.csv"
car_in = "D:/workspace/python/test/01_实证网络_train_car_plane/data/car_in.csv"

d_value=main_Quantification_02.D_value(0.45,0.45,0.1,car_in,train_in,"car_in","train_in")
print("d_value",d_value)
d_value_true=np.round(d_value,3)
print("保留两位小数:",np.real(d_value_true))
