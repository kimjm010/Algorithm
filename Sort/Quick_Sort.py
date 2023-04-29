# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정령 알고리즘 중 하나
# 병합 정령과 더불어 대부분의 프로그래밍 언어의 정령 라이브러리의 근간이 되는 알고리즘
# 가장 기본적은 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정함



def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left_index = start + 1
    right_index = end
    while(left_index <= right_index):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left_index <= end and array[left_index] <= array[pivot]):
            left_index += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right_index > start and array[right_index] >= array[pivot]):
            right_index -= 1
        if (left_index > right_index): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right_index], array[pivot] = array[pivot], array[right_index]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left_index], array[right_index] = array[right_index], array[left_index]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정령 수행
    quick_sort(array, start, right_index - 1)
    quick_sort(array, right_index + 1, end)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)


def simple_quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return simple_quick_sort(left_side) + [pivot] + simple_quick_sort(right_side)
print(simple_quick_sort(array))