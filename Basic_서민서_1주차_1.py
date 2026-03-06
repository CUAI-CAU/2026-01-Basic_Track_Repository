import numpy as np

array1 = np.array([1,2,3])
print('array1 type:', type(array1))
print('array1 array 형태:',array1.shape)

'''
넘파이를 np로 호출. 배열의 타입, 형태를 출력
1차원 배열이 만들어짐
'''

array2 = np.array([[1,2,3],[2,3,4]])
print('array2 type:', type(array2))
print('array2 array 형태:',array2.shape)

'''
2차원 배열이 만들어짐 (2개의 행과 3개의 열) 
'''

array3 = np.array([[1,2,3]])
print('array3 type:', type(array3))
print('array3 array 형태:',array3.shape)

'''
2차원 배열이 만들어짐 (1개의 행과 3개의 열)
'''

print('array1: {0}차원, array2: {1}차원, array3: {2}차원'.format(array1.ndim, array2.ndim, array3.ndim))

'''
ndim을 통해 배열의 차원을 출력함 ([] 개수가 곧 차원의 수임!)
'''

list1 = [1,2,3]
print(type(list1))
array1 = np.array(list1)
print(type(array1))
print(array1, array1.dtype)

'''
리스트를 넘파이 배열로 전환 후 타입과 데이터 타입을 출력함
'''

list2 = [1,2,'test']
array2 = np.array(list2)
print(array2,array2.dtype)

list3 = [1,2,3.0]
array3 = np.array(list3)
print(array3,array3.dtype)

'''
리스트에 문자열이 포함되면 전체가 문자열로 변환되고, 실수가 포함되면 전체가 실수로 변환됨
'''

array_int = np.array([1,2,3])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

'''정수형 배열을 실수형으로 변환함
'''

array_int1 = array_float.astype('int32')
print(array_int1, array_int1.dtype)

'''실수형 배열을 정수형으로 변환함
'''

array_float1 = np.array([1.1,2.2,3.1])
array_int2 = array_float1.astype('int32')
print(array_int2, array_int2.dtype)

'''실수형 배열을 정수형으로 변환할 때 소수점 이하가 버려짐
'''

sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

'''
arange 함수를 활용해 1차원 배열 생성. 데이터타입은 int, 형태는 (10,)'''

zero_array = np.zeros((3,2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

'''
zeros 함수를 활용한 영행렬 생성. 데이터타입은 int로 지정, 형태는 (3,2)'''

one_array = np.ones((3,2))
print(one_array)
print(one_array.dtype, one_array.shape)

'''ones 함수를 활용한 일행렬 생성. 데이터타입은 default로 float, 형태는 (3,2)'''

array1  =np.arange(10)
print('array1:\n', array1)

'''arange 함수를 활용해 0부터 9까지의 정수로 이루어진 1차원 배열 생성. \n은 줄바꿈을 의미함'''

array2 = array1.reshape(2,5)
print('array2:\n', array2)

'''reshape 함수를 활용해 array1을 2행 5열의 2차원 배열로 변환함'''

array3 = array1.reshape(5,2)
print('array3:\n', array3)

'''reshape 함수를 활용해 array1을 5행 2열의 2차원 배열로 변환함'''

array1 = np.arange(10)
print(array1)
array2 = array1.reshape(-1,5)
print('array2 shape:',array2.shape)
array3 = array1.reshape(5,-1)
print('array3 shape:',array3.shape)

'''reshape 함수에서 -1을 사용하면 해당 차원의 크기를 자동으로 계산함. array2는 2행 5열, array3는 5행 2열이 됨
'''

'''
array1 = np.arange(10)
array2 = array1.reshape(-1,4)
print('array2 shape:',array2.shape)

에러를 유발하는 코드. reshape 함수는 변환이 불가하면 ValueError를 발생시키는데, array1의 원소 수는 10개이므로 4열로 변환할 수 없음
'''

array1 = np.arange(8)
array3d = array1.reshape((2,2,2))
print('array3d:\n', array3d.tolist())

'''array1을 2행 2열 2채널의 3차원 배열로 변환함. tolist() 함수를 활용해 배열을 리스트 형태로 출력함'''

array5 = array3d.reshape(-1,1)
print('array5:\n', array5.tolist())
print('array5 shape:', array5.shape)

'''array3d를 1열로 변환함. tolist() 함수를 활용해 배열을 리스트 형태로 출력함. array5는 8행 1열의 2차원 배열이 됨'''

array6 = array1.reshape(-1,1)
print('array6:\n', array6.tolist())
print('array6 shape:', array6.shape)

'''array1을 1열로 변환함. tolist() 함수를 활용해 배열을 리스트 형태로 출력함. array6는 8행 1열의 2차원 배열이 됨'''

array1 = np.arange(start=1, stop=10)
print('array1:',array1)

'''arange 함수를 활용해 1부터 9까지의 정수로 이루어진 1차원 배열 생성. stop은 포함되지 않음'''

value = array1[2]
print('value:', value)
print(type(value))

'''array1의 3번째 원소를 value에 저장함. 인덱스는 0부터 시작하므로 array1[2]는 3번째 원소인 3이 됨. value의 타입은 numpy.int64임
'''

array1[1] = 9
array1[8] = 0
print('array1:', array1)

'''array1의 2번째 원소를 9로, 9번째 원소를 0으로 변경함. array1은 [1, 9, 3, 4, 5, 6, 7, 8, 0]이 됨
'''

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3,3)
print(array2d)

'''arange 함수를 활용해 1부터 9까지의 정수로 이루어진 1차원 배열을 생성한 후 reshape 함수를 활용해 3행 3열의 2차원 배열로 변환함. array2d는 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 됨
'''

print('(row=0, col=0) index 가리키는 값:', array2d[0,0])
print('(row=0, col=1) index 가리키는 값:', array2d[0,1])
print('(row=1, col=0) index 가리키는 값:', array2d[1,0])
print('(row=2, col=2) index 가리키는 값:', array2d[2,2])

'''array2d의 각 원소에 접근하여 값을 출력함. array2d[0,0]은 1, array2d[0,1]은 2, array2d[1,0]은 4, array2d[2,2]는 9가 됨
'''

array1 = np.arange(start=1, stop=10)
array4 = array1[:3]
print(array4)

'''array1의 처음부터 3번째 원소까지 슬라이싱하여 array4에 저장함. array4는 [1, 2, 3]이 됨'''

array5 = array1[3:]
print(array5)

'''array1의 4번째 원소부터 끝까지 슬라이싱하여 array5에 저장함. array5는 [4, 5, 6, 7, 8, 9]가 됨'''

array6 = array1[:]
print(array6)

'''array1의 모든 원소를 슬라이싱하여 array6에 저장함. array6는 [1, 2, 3, 4, 5, 6, 7, 8, 9]가 됨'''

array1d = np.arrange(start=1, stop=10)
array2d = array1d.reshape(3,3)
print('array2d:\n', array2d)

'''arange 함수를 활용해 1부터 9까지의 정수로 이루어진 1차원 배열을 생성한 후 reshape 함수를 활용해 3행 3열의 2차원 배열로 변환함. array2d는 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 됨
'''

print('array2d[0:2, 0:2]:\n', array2d[0:2, 0:2])
'''array2d의 0행부터 1행까지, 0열부터 1열까지 슬라이싱하여 출력함. array2d[0:2, 0:2]는 [[1, 2], [4, 5]]가 됨
'''

print('array2d[1:3, 0:3]:\n', array2d[1:3, 0:3])
'''array2d의 1행부터 2행까지, 0열부터 2열까지 슬라이싱하여 출력함. array2d[1:3, 0:3]는 [[4, 5, 6], [7, 8, 9]]가 됨
'''

print('array2d[1:3, :]:\n', array2d[1:3, :])
'''array2d의 1행부터 2행까지, 모든 열을 슬라이싱하여 출력함. array2d[1:3, :]는 [[4, 5, 6], [7, 8, 9]]가 됨
'''

print('array2d[:, :]:\n', array2d[:, :])
'''array2d의 모든 행과 모든 열을 슬라이싱하여 출력함. array2d[:, :]는 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 됨
'''

print('array2d[:2, 1:]:\n', array2d[:2, 1:])
'''array2d의 처음부터 1행까지, 1열부터 끝까지 슬라이싱하여 출력함. array2d[:2, 1:]는 [[2, 3], [5, 6]]가 됨
'''

print('array2d[:2, 0]:\n', array2d[:2, 0])
'''array2d의 처음부터 1행까지, 0열을 슬라이싱하여 출력함. array2d[:2, 0]는 [1, 4]가 됨
'''

print(array2d[0])
'''array2d의 0행을 출력함. array2d[0]은 [1, 2, 3]이 됨
'''

print(array2d[1])
'''array2d의 1행을 출력함. array2d[1]은 [4, 5, 6]이 됨
'''

print('array2d[0] shape:', array2d[0].shape, 'array2d[1] shape:', array2d[1].shape)
'''array2d[0]과 array2d[1]의 형태를 출력함'''

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3,3)

'''arange 함수를 활용해 1부터 9까지의 정수로 이루어진 1차원 배열을 생성한 후 reshape 함수를 활용해 3행 3열의 2차원 배열로 변환함. array2d는 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 됨'''

array3 = array2d[[0,1],2]
print('array2d[[0,1],2] => ', array3.tolist())
'''array2d의 0행과 1행에서 2열에 해당하는 원소를 선택하여 array3에 저장함. array3는 [3, 6]이 됨
'''

array4 = array2d[[0,1], 0:2]
print('array2d[[0,1], 0:2] => ', array4.tolist())
'''array2d의 0행과 1행에서 0열부터 1열까지 슬라이싱하여 array4에 저장함. array4는 [[1, 2], [4, 5]]가 됨
'''

array5 = array2d[[0,1]]
print('array2d[[0,1]] => ', array5.tolist())
'''array2d의 0행과 1행을 선택하여 array5에 저장함. array5는 [[1, 2, 3], [4, 5, 6]]가 됨
'''

array1d = np.arange(start=1, stop=10)
array3 = array1d[array1d > 5]
print('array1d > 5 불린 인덱싱 결과 값:', array3)

'''array1d에서 5보다 큰 원소를 불린 인덱싱하여 array3에 저장함. array3는 [6, 7, 8, 9]가 됨'''

array1d > 5
'''array1d에서 5보다 큰 원소에 대해 True, 그렇지 않은 원소에 대해 False를 반환함. 결과는 [False, False, False, False, False, True, True, True, True]가 됨
'''

boolean_indexes = np.array([False, False, False, False, False, True, True, True, True])
array3 = array1d[boolean_indexes]
print('불린 인덱스로 필터링 결과:', array3)

'''boolean_indexes 배열을 활용해 array1d에서 5보다 큰 원소를 필터링하여 array3에 저장함. array3는 [6, 7, 8, 9]가 됨
'''

indexes = np.array([5,6,7,8])
array4 = array1d[indexes]
print('일반 인덱스로 필터링 결과:', array4)

'''indexes 배열을 활용해 array1d에서 5번째부터 8번째 원소를 필터링하여 array4에 저장함. array4는 [6, 7, 8, 9]가 됨'''

org_array = np.array([3,1,9,5])
print('원본 배열:', org_array)
sort_array1 = np.sort(org_array)
print('np.sort()로 정렬한 결과:', sort_array1)

'''org_array를 np.sort() 함수를 활용해 정렬하여 sort_array1에 저장함. sort_array1는 [1, 3, 5, 9]가 됨
'''

print('원본 배열:', org_array)
sort_array2 = org_array.sort()
print('ndarray.sort()로 정렬한 결과:', sort_array2)
print('원본 배열 after ndarray.sort():', org_array)

'''org_array를 ndarray.sort() 메서드를 활용해 정렬하여 sort_array2에 저장함. sort_array2는 None이 됨. org_array는 [1, 3, 5, 9]로 정렬됨
'''

'''이로서 np.sort() 함수는 원본 배열을 변경하지 않고 정렬된 배열을 반환하는 반면, ndarray.sort() 메서드는 원본 배열을 직접 정렬하고 None을 반환한다는 것을 알 수 있음'''

sort_array1_desc = np.sort(org_array)[::-1]
print('내림차순으로 정렬한 결과:', sort_array1_desc)

'''np.sort() 함수를 활용해 org_array를 정렬한 후 슬라이싱을 활용해 내림차순으로 정렬된 배열을 sort_array1_desc에 저장함. sort_array1_desc는 [9, 5, 3, 1]이 됨'''

array2d = np.array([[8,12],[7,1]])

sort_array2d_axis0 = np.sort(array2d, axis=0)
print('행 방향으로 정렬:\n', sort_array2d_axis0)

sort_array2d_axis1 = np.sort(array2d, axis=1)
print('열 방향으로 정렬:\n', sort_array2d_axis1)

'''array2d를 행 방향으로 정렬하여 sort_array2d_axis0에 저장함. sort_array2d_axis0는 [[7, 1], [8, 12]]가 됨. 
array2d를 열 방향으로 정렬하여 sort_array2d_axis1에 저장함. sort_array2d_axis1는 [[8, 12], [1, 7]]가 됨'''

org_arrray = np.array([3,1,9,5])
sort_indices = np.argsort(org_array)
print(type(sort_indices))
print('행렬 정렬 시 원본 행렬의 인덱스:', sort_indices)

'''org_array를 np.argsort() 함수를 활용해 정렬할 때 원본 배열의 인덱스를 반환하여 sort_indices에 저장함. sort_indices는 [1, 0, 3, 2]가 됨
'''

org_array = np.array([3,1,9,5])
sort_indices_desc = np.argsort(org_array)[::-1]
print('내림차순으로 정렬 시 원본 행렬의 인덱스:', sort_indices_desc)

'''org_array를 np.argsort() 함수를 활용해 정렬한 후 슬라이싱을 활용해 내림차순으로 정렬할 때 원본 배열의 인덱스를 반환하여 sort_indices_desc에 저장함. sort_indices_desc는 [2, 3, 0, 1]이 됨'''

import numpy as np

name_array = np.array(['John', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array = np.array([78,95,84,98,88])

sort_indices = np.argsort(score_array)
print('성적 오름차순 정렬 시 score_array의 인덱스:', sort_indices)
print('성적 오름차순으로 name_array의 이름 출력:', name_array[sort_indices])

'''score_array를 np.argsort() 함수를 활용해 정렬할 때 원본 배열의 인덱스를 반환하여 sort_indices에 저장함. sort_indices는 [0, 2, 4, 1, 3]이 됨.
sort_indices를 활용해 name_array에서 성적이 낮은 순서대로 이름을 출력함. 결과는 ['John', 'Sarah', 'Samuel', 'Mike', 'Kate']가 됨
'''

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])

dot_product = np.dot(A,B)
print('행렬 내적 결과:\n', dot_product)

'''A와 B의 행렬 내적을 np.dot() 함수를 활용해 계산하여 dot_product에 저장함. 
dot_product는 [[58, 64], [139, 154]]가 됨'''

A = np.array([[1,2,],[3,4]])
transpose_mat = np.transpose(A)
print('A의 전치 행렬:\n', transpose_mat)

'''A의 전치 행렬을 np.transpose() 함수를 활용해 계산하여 transpose_mat에 저장함.'''
