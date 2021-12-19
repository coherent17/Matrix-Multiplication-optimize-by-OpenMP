import numpy as np
import matplotlib.pyplot as plt
import math as m

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

def plot_6_method(cpu_num, ijk,jik,jki,kji,kij,ikj,size):
    plt.subplot(1, 2, 1)
    plt.plot(cpu_num,ijk,'-D',label='ijk method',linewidth=4,markersize=12)
    plt.plot(cpu_num,jik,'-v',label='jik method',linewidth=4,markersize=12)
    plt.plot(cpu_num,jki,'-p',label='jki method',linewidth=4,markersize=12)
    plt.plot(cpu_num,kji,'-*',label='kji method',linewidth=4,markersize=14)
    plt.plot(cpu_num,kij,'-o',label='kij method',linewidth=4,markersize=12)
    plt.plot(cpu_num,ikj,'-s',label='ikj method',linewidth=4,markersize=12)
    plt.xlabel('CPU number',fontsize=24)
    plt.ylabel('Time(Sec)',fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Execution time (Matrix size = %d x %d)" %(size,size),fontsize=24)
    plt.grid(True)
    plt.legend(fontsize=18)

    plt.subplot(1, 2, 2)
    plt.plot(cpu_num,1/(ijk/ijk[0]),'-D',label='ijk method',linewidth=4,markersize=12)
    plt.plot(cpu_num,1/(jik/jik[0]),'-v',label='jik method',linewidth=4,markersize=12)
    plt.plot(cpu_num,1/(jki/jki[0]),'-p',label='jki method',linewidth=4,markersize=12)
    plt.plot(cpu_num,1/(kji/kji[0]),'-*',label='kji method',linewidth=4,markersize=14)
    plt.plot(cpu_num,1/(kij/kij[0]),'-o',label='kij method',linewidth=4,markersize=12)
    plt.plot(cpu_num,1/(ikj/ikj[0]),'-s',label='ikj method',linewidth=4,markersize=12)
    plt.xlabel('CPU number',fontsize=24)
    plt.ylabel('$Performance/Performance_{using 1 CPU}$',fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Performance (Matrix size = %d x %d)" %(size,size),fontsize=24)
    plt.grid(True)
    plt.legend(fontsize=18)
    plt.show()

def plot_cpu(matrix_size,CPU_index):
    ijk = np.array([ijk_256[CPU_index],ijk_512[CPU_index],ijk_1024[CPU_index],ijk_2048[CPU_index]])
    jik = np.array([jik_256[CPU_index],jik_512[CPU_index],jik_1024[CPU_index],jik_2048[CPU_index]])
    jki = np.array([jki_256[CPU_index],jki_512[CPU_index],jki_1024[CPU_index],jki_2048[CPU_index]])
    kji = np.array([kji_256[CPU_index],kji_512[CPU_index],kji_1024[CPU_index],kji_2048[CPU_index]])
    kij = np.array([kij_256[CPU_index],kij_512[CPU_index],kij_1024[CPU_index],kij_2048[CPU_index]])
    ikj = np.array([ikj_256[CPU_index],ikj_512[CPU_index],ikj_1024[CPU_index],ikj_2048[CPU_index]])
    plt.plot(matrix_size,ijk,'-D',label='ijk method',linewidth=3,markersize=10)
    plt.plot(matrix_size,jik,'-v',label='jik method',linewidth=3,markersize=10)
    plt.plot(matrix_size,jki,'-p',label='jki method',linewidth=3,markersize=10)
    plt.plot(matrix_size,kji,'-*',label='kji method',linewidth=3,markersize=10)
    plt.plot(matrix_size,kij,'-o',label='kij method',linewidth=5,markersize=13)
    plt.plot(matrix_size,ikj,'-s',label='ikj method',linewidth=3,markersize=10)
    plt.xticks(matrix_size,fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel('lg(square matrix.length)',fontsize=16)
    plt.ylabel('Time(Sec)',fontsize=16)
    plt.title('Matrix size v.s. Execution time (%d CPU)' %(CPU_index+1),fontsize=24)
    plt.legend(fontsize=16)
    plt.grid(True)

# a. matrix size = 2048 * 2048
plot_6_method(cpu_num,ijk_2048,jik_2048,jki_2048,kji_2048,kij_2048,ikj_2048,2048)

# b. matrix size = 1024 * 1024
plot_6_method(cpu_num,ijk_1024,jik_1024,jki_1024,kji_1024,kij_1024,ikj_1024,1024)

# c. matrix size = 512 * 512
plot_6_method(cpu_num,ijk_512,jik_512,jki_512,kji_512,kij_512,ikj_512,512)

# d. matrix size = 256 * 256
plot_6_method(cpu_num,ijk_256,jik_256,jki_256,kji_256,kij_256,ikj_256,256)

# e. matrix size = 128 * 128
plot_6_method(cpu_num,ijk_128,jik_128,jki_128,kji_128,kij_128,ikj_128,128)

# matrix size analysis
matrix_size = np.array([m.log(256,2),m.log(512,2),m.log(1024,2),m.log(2048,2)])
# a. using 1 CPU
plt.subplot(2, 2, 1)
plot_cpu(matrix_size,0)

# b. using 2 CPU
plt.subplot(2, 2, 2)
plot_cpu(matrix_size,1)

# c. using 3 CPU
plt.subplot(2, 2, 3)
plot_cpu(matrix_size,2)

# d. using 4 CPU
plt.subplot(2, 2, 4)
plot_cpu(matrix_size,3)

plt.show()