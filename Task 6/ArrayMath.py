import numpy 
numpy.set_printoptions(legacy='1.13')
N,M=map(int,input().strip().split(' '))
arr_N, arr_M =(numpy.array([list(input().split()) for _ in range(N)], dtype=int) for _ in range(2))
print(numpy.add(arr_N,arr_M))
print(numpy.subtract(arr_N,arr_M))
print(numpy.multiply(arr_N,arr_M))
print(numpy.floor_divide(arr_N,arr_M))
print(numpy.mod(arr_N,arr_M))
print(numpy.power(arr_N,arr_M))