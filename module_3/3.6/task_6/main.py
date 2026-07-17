def merge_sorted_lists(first_list, second_list):
    merged_list = []
    first_index = 0
    second_index = 0

    while first_index < len(first_list) or second_index < len(second_list):
        if second_index == len(second_list):
            next_number = first_list[first_index]
            first_index += 1
        elif first_index == len(first_list):
            next_number = second_list[second_index]
            second_index += 1
        elif first_list[first_index] <= second_list[second_index]:
            next_number = first_list[first_index]
            first_index += 1
        else:
            next_number = second_list[second_index]
            second_index += 1

        if not merged_list or merged_list[-1] != next_number:
            merged_list.append(next_number)

    return merged_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
