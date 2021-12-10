import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape

data_128 = np.genfromtxt('dataset_128.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_256 = np.genfromtxt('dataset_256.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_512 = np.genfromtxt('dataset_512.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_1024 = np.genfromtxt('dataset_1024.csv', delimiter=',',encoding='UTF-8',skip_header=1)
data_2048 = np.genfromtxt('dataset_2048.csv', delimiter=',',encoding='UTF-8',skip_header=1)

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

# locality analysis

# a. matrix size = 2048
plt.subplot(1, 2, 1)
plt.plot(cpu_num,ijk_2048,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,jik_2048,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,jki_2048,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,kji_2048,'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,kij_2048,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,ikj_2048,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title("Spatial locality v.s. Execution time (Matrix size = 2048)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)


plt.subplot(1, 2, 2)
plt.plot(cpu_num,1/(ijk_2048/ijk_2048[0]),'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jik_2048/jik_2048[0]),'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jki_2048/jki_2048[0]),'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(kji_2048/kji_2048[0]),'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,1/(kij_2048/kij_2048[0]),'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(ikj_2048/ikj_2048[0]),'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Performance/Performance on 1 CPU',fontsize=16)
plt.title("Spatial locality v.s. Performance (Matrix size = 2048)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)
plt.show()


# b. matrix size = 1024
plt.subplot(1, 2, 1)
plt.plot(cpu_num,ijk_1024,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,jik_1024,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,jki_1024,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,kji_1024,'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,kij_1024,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,ikj_1024,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title("Spatial locality v.s. Execution time (Matrix size = 1024)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)


plt.subplot(1, 2, 2)
plt.plot(cpu_num,1/(ijk_1024/ijk_1024[0]),'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jik_1024/jik_1024[0]),'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jki_1024/jki_1024[0]),'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(kji_1024/kji_1024[0]),'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,1/(kij_1024/kij_1024[0]),'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(ikj_1024/ikj_1024[0]),'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Performance/Performance on 1 CPU',fontsize=16)
plt.title("Spatial locality v.s. Performance (Matrix size = 1024)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)

plt.show()

# c. matrix size = 512
plt.subplot(1, 2, 1)
plt.plot(cpu_num,ijk_512,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,jik_512,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,jki_512,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,kji_512,'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,kij_512,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,ikj_512,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title("Spatial locality v.s. Execution time (Matrix size = 512)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)


plt.subplot(1, 2, 2)
plt.plot(cpu_num,1/(ijk_512/ijk_512[0]),'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jik_512/jik_512[0]),'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jki_512/jki_512[0]),'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(kji_512/kji_512[0]),'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,1/(kij_512/kij_512[0]),'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(ikj_512/ikj_512[0]),'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Performance/Performance on 1 CPU',fontsize=16)
plt.title("Spatial locality v.s. Performance (Matrix size = 512)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)

plt.show()

# d. matrix size = 256
plt.subplot(1, 2, 1)
plt.plot(cpu_num,ijk_256,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,jik_256,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,jki_256,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,kji_256,'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,kij_256,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,ikj_256,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title("Spatial locality v.s. Execution time (Matrix size = 256)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)


plt.subplot(1, 2, 2)
plt.plot(cpu_num,1/(ijk_256/ijk_256[0]),'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jik_256/jik_256[0]),'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jki_256/jki_256[0]),'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(kji_256/kji_256[0]),'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,1/(kij_256/kij_256[0]),'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(ikj_256/ikj_256[0]),'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Performance/Performance on 1 CPU',fontsize=16)
plt.title("Spatial locality v.s. Performance (Matrix size = 256)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)

plt.show()

# e. matrix size = 128
plt.subplot(1, 2, 1)
plt.plot(cpu_num,ijk_128,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,jik_128,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,jki_128,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,kji_128,'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,kij_128,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,ikj_128,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title("Spatial locality v.s. Execution time (Matrix size = 128)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)


plt.subplot(1, 2, 2)
plt.plot(cpu_num,1/(ijk_128/ijk_128[0]),'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jik_128/jik_128[0]),'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(jki_128/jki_128[0]),'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(kji_128/kji_128[0]),'-*',label='kji method',linewidth=3,markersize=12)
plt.plot(cpu_num,1/(kij_128/kij_128[0]),'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(cpu_num,1/(ikj_128/ikj_128[0]),'-s',label='ikj method',linewidth=3,markersize=10)
plt.xlabel('CPU number',fontsize=16)
plt.ylabel('Performance/Performance on 1 CPU',fontsize=16)
plt.title("Spatial locality v.s. Performance (Matrix size = 128)",fontsize=24)
plt.grid(True)
plt.legend(fontsize=16)

plt.show()

# matrix size analysis
