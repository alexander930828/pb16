def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i] # i번 위치에 있는 값을 key에 저장 // save the value in position to key
        # j 를 i 바로 왼쪽 위치로 저장
        j = i - 1
        while j >= 0 and a[j] > key: # a[j]: 비교할 값보다 앞에 있는값 / key = [a[i]]로 뒤에있는 값 만약 앞에있는 값이 더크게되면,
            a[j + 1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동해버리고
            j -= 1
        a[j + 1] = key # 찾은 위치에 key를 저장

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)