def solution(int_arr):
    int_arr_len = len(int_arr)
    sum_array = [1 for i in int_arr_len]
    for i in range(int_arr_len):
        for j in range(int_arr_len):
            if i != j:
                sum_array[i] *= int_arr[j]
    return sum_array


if __name__ == '__main__':
    int_numbers = [3, 2, 1]
    print(solution(int_numbers))
