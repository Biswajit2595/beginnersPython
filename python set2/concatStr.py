def concatenate_lists_indexwise(list1, list2):
    result = []
    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        result.append(list1[i] + list2[i])

    # Add any leftover items from list1 or list2
    result.extend(list1[min_len:])
    result.extend(list2[min_len:])

    return result

# Given inputs
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = concatenate_lists_indexwise(list1, list2)
print(result)
