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
# a. using 1 CPU
ijk_1CPU = np.array([ijk_256[0],ijk_512[0],ijk_1024[0],ijk_2048[0]])
jik_1CPU = np.array([jik_256[0],jik_512[0],jik_1024[0],jik_2048[0]])
jki_1CPU = np.array([jki_256[0],jki_512[0],jki_1024[0],jki_2048[0]])
kji_1CPU = np.array([kji_256[0],kji_512[0],kji_1024[0],kji_2048[0]])
kij_1CPU = np.array([kij_256[0],kij_512[0],kij_1024[0],kij_2048[0]])
ikj_1CPU = np.array([ikj_256[0],ikj_512[0],ikj_1024[0],ikj_2048[0]])
matrix_size = np.array([m.log(256,2),m.log(512,2),m.log(1024,2),m.log(2048,2)])
plt.plot(matrix_size,ijk_1CPU,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(matrix_size,jik_1CPU,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(matrix_size,jki_1CPU,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(matrix_size,kji_1CPU,'-*',label='kji method',linewidth=3,markersize=10)
plt.plot(matrix_size,kij_1CPU,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(matrix_size,ikj_1CPU,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xticks(matrix_size)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title('Matrix size v.s. Execution time (1 CPU)',fontsize=24)
plt.legend(fontsize=16)
plt.grid(True)
plt.show()

# b. using 2 CPU
ijk_2CPU = np.array([ijk_256[1],ijk_512[1],ijk_1024[1],ijk_2048[1]])
jik_2CPU = np.array([jik_256[1],jik_512[1],jik_1024[1],jik_2048[1]])
jki_2CPU = np.array([jki_256[1],jki_512[1],jki_1024[1],jki_2048[1]])
kji_2CPU = np.array([kji_256[1],kji_512[1],kji_1024[1],kji_2048[1]])
kij_2CPU = np.array([kij_256[1],kij_512[1],kij_1024[1],kij_2048[1]])
ikj_2CPU = np.array([ikj_256[1],ikj_512[1],ikj_1024[1],ikj_2048[1]])
matrix_size = np.array([m.log(256,2),m.log(512,2),m.log(1024,2),m.log(2048,2)])
plt.plot(matrix_size,ijk_2CPU,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(matrix_size,jik_2CPU,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(matrix_size,jki_2CPU,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(matrix_size,kji_2CPU,'-*',label='kji method',linewidth=3,markersize=10)
plt.plot(matrix_size,kij_2CPU,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(matrix_size,ikj_2CPU,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xticks(matrix_size)
plt.ylabel('Time(Sec)',fontsize=16)
plt.title('Matrix size v.s. Execution time (2 CPU)',fontsize=24)
plt.legend(fontsize=16)
plt.grid(True)
plt.show()

# c. using 3 CPU
ijk_3CPU = np.array([ijk_256[2],ijk_512[2],ijk_1024[2],ijk_2048[2]])
jik_3CPU = np.array([jik_256[2],jik_512[2],jik_1024[2],jik_2048[2]])
jki_3CPU = np.array([jki_256[2],jki_512[2],jki_1024[2],jki_2048[2]])
kji_3CPU = np.array([kji_256[2],kji_512[2],kji_1024[2],kji_2048[2]])
kij_3CPU = np.array([kij_256[2],kij_512[2],kij_1024[2],kij_2048[2]])
ikj_3CPU = np.array([ikj_256[2],ikj_512[2],ikj_1024[2],ikj_2048[2]])
matrix_size = np.array([m.log(256,2),m.log(512,2),m.log(1024,2),m.log(2048,2)])
plt.plot(matrix_size,ijk_3CPU,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(matrix_size,jik_3CPU,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(matrix_size,jki_3CPU,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(matrix_size,kji_3CPU,'-*',label='kji method',linewidth=3,markersize=10)
plt.plot(matrix_size,kij_3CPU,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(matrix_size,ikj_3CPU,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xticks(matrix_size)
plt.ylabel('Time(Sec)',fontsize=16)
plt.xlabel('lg(square matrix.length)',fontsize=16)
plt.title('Matrix size v.s. Execution time (3 CPU)',fontsize=24)
plt.legend(fontsize=16)
plt.grid(True)
plt.show()

# d. using 4 CPU
ijk_4CPU = np.array([ijk_256[3],ijk_512[3],ijk_1024[3],ijk_2048[3]])
jik_4CPU = np.array([jik_256[3],jik_512[3],jik_1024[3],jik_2048[3]])
jki_4CPU = np.array([jki_256[3],jki_512[3],jki_1024[3],jki_2048[3]])
kji_4CPU = np.array([kji_256[3],kji_512[3],kji_1024[3],kji_2048[3]])
kij_4CPU = np.array([kij_256[3],kij_512[3],kij_1024[3],kij_2048[3]])
ikj_4CPU = np.array([ikj_256[3],ikj_512[3],ikj_1024[3],ikj_2048[3]])
matrix_size = np.array([m.log(256,2),m.log(512,2),m.log(1024,2),m.log(2048,2)])
plt.plot(matrix_size,ijk_4CPU,'-o',label='ijk method',linewidth=3,markersize=10)
plt.plot(matrix_size,jik_4CPU,'-v',label='jik method',linewidth=3,markersize=10)
plt.plot(matrix_size,jki_4CPU,'-p',label='jki method',linewidth=3,markersize=10)
plt.plot(matrix_size,kji_4CPU,'-*',label='kji method',linewidth=3,markersize=10)
plt.plot(matrix_size,kij_4CPU,'-D',label='kij method',linewidth=3,markersize=10)
plt.plot(matrix_size,ikj_4CPU,'-s',label='ikj method',linewidth=3,markersize=10)
plt.xticks(matrix_size)
plt.ylabel('Time(Sec)',fontsize=16)
plt.xlabel('lg(square matrix.length)',fontsize=16)
plt.title('Matrix size v.s. Execution time (4 CPU)',fontsize=24)
plt.legend(fontsize=16,loc='upper left')
plt.grid(True)
plt.show()
plt.show()