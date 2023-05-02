# def print_max(first_array, second_array, k):
#     first_array.sort()
#     second_array.sort(reversed)
#     result = 0
    
#     if first_array[0] >= second_array[-1]:
#         for i in range(0, len(first_array) - 1):
#             result += first_array[i]
#     else:
#         first_array[0], second_array[-1] = second_array[-1], first_array[0]
#         first_array[1], second_array[-2] = second_array[-2], first_array[1]
#         first_array[2], second_array[-3] = second_array[-3], first_array[2]
#         for i in range(0, len(first_array) - 1):
#             result += first_array[i]
#     return result


# array1 = [1, 2, 5, 4, 3]
# array2 = [5, 5, 6, 6, 5]
# print_max(array1, array2, 3)

n, k = map(int, input().split()) # N,K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력 받기

a.sort() # 배열 A는 오름차순으로 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순으로 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))