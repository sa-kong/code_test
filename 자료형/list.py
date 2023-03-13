# 리스트 컴프리헨션
array = [i for i in range(10)]
array = [i for i in range(20) if i %2 == 1]
array = [i * i for i in range(1, 10)]

m=10
n=5
array = [[0]*m for _ in range(n)]
# array = [[0]*m]*n 인 경우 형태는 같으나 열마다 같은 객채로 데이터 값이 모든 열에서 동시에 변경된다.
#_ : 반복을 수행하되 반복을 위한 변수 값을 무시하는 경우 주로 사용
# for _ in range(5):
#   print("Hello!!")
print(array)