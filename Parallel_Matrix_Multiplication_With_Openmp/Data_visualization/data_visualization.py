import numpy as np
import matplotlib.pyplot as plt

data_128 = np.genfromtxt('dataset_128.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_256 = np.genfromtxt('dataset_256.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_512 = np.genfromtxt('dataset_512.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_1024 = np.genfromtxt('dataset_1024.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_2048 = np.genfromtxt('dataset_2048.csv', delimiter=',',encoding='UTF-8',skip_header=1)

print(data_128)
print(data_256)
print(data_512)
print(data_1024)
print(data_2048)

cpu_num = np.array([1,2,3,4,5,6,7,8])
cpu_num = np.reshape(cpu_num,8)

ijk_128 = data_128[0,:] * 10**-3
ijk_256 = data_256[0,:] * 10**-3
ijk_512 = data_512[0,:]
ijk_1024 = data_1024[0,:]
ijk_2048 = data_2048[0,:]

jik_128 = data_128[1,:] * 10**-3
jik_256 = data_256[1,:] * 10**-3
jik_512 = data_512[1,:]
jik_1024 = data_1024[1,:]
jik_2048 = data_2048[1,:]

jki_128 = data_128[2,:] * 10**-3
jki_256 = data_256[2,:] * 10**-3
jki_512 = data_512[2,:]
jki_1024 = data_1024[2,:]
jki_2048 = data_2048[2,:]

kji_128 = data_128[3,:] * 10**-3
kji_256 = data_256[3,:] * 10**-3
kji_512 = data_512[3,:]
kji_1024 = data_1024[3,:]
kji_2048 = data_2048[3,:]

kij_128 = data_128[4,:] * 10**-3
kij_256 = data_256[4,:] * 10**-3
kij_512 = data_512[4,:]
kij_1024 = data_1024[4,:]
kij_2048 = data_2048[4,:]

ikj_128 = data_128[5,:] * 10**-3
ikj_256 = data_256[5,:] * 10**-3
ikj_512 = data_512[5,:]
ikj_1024 = data_1024[5,:]
ikj_2048 = data_2048[5,:]

plt.plot(cpu_num,ikj_1024)
plt.plot(cpu_num,jik_1024)
plt.plot(cpu_num,jki_1024)
plt.plot(cpu_num,kji_1024)
plt.plot(cpu_num,kij_1024)
plt.plot(cpu_num,ikj_1024)
plt.xlabel('cpu_num')
plt.ylabel('time')

plt.show()