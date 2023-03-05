def solution(num_list, k):
    list_len = len(num_list)
    for i in range(list_len-1):
        for j in range(i+1, list_len):
            if num_list[i] + num_list[j] == k:
                return True
    return False


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    curr_k = 10
    is_any_sum_equals_k = solution(numbers, curr_k)
    print('Is the sum of any pair of elements equals k?', is_any_sum_equals_k)
