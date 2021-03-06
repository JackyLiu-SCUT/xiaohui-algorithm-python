

def bucket_sort(array=[]):
    # 1.得到数列的最大值和最小值，并计算出差值d
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    # 2.初始化桶
    bucket_num = len(array)
    bucket_list = []
    for i in range(0, bucket_num):
        bucket_list.append([])
    # 3.遍历原始数组，将每个元素放入桶中
    for i in range(0, len(array)):
        num = int((array[i] - min_value) * (bucket_num - 1) / d) # num计算出当前数属于哪个桶，即bucket_list的下标，这是因为区间跨度=（最大值-最小值）/（桶的数量-1），所以num=（当前数-最小值）/ 区间跨度
        bucket = bucket_list[num]
        bucket.append(array[i])
    # 4.对每个桶内部进行排序
    for i in range(0, len(bucket_list)):
        # list采用了归并排序或归并的优化版本
        bucket_list.sort()
    # 5.输出全部元素
    sorted_array = []
    for sub_list in bucket_list:
        for element in sub_list:
            sorted_array.append(element)
    return sorted_array

my_array = list([4.22, 6.421, 0.0023, 3.0, 2.213, 8.122, 4.12, 10.09])
print(bucket_sort(my_array))