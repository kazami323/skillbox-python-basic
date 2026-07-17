nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
]

flattened_list = [number
                  for large_list in nice_list
                  for small_list in large_list
                  for number in small_list]

print(flattened_list)
