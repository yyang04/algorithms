















def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(l1, l2):
    merged = []
    while l1 and l2:
        if l1[0] < l2[0]:
            merged.append(l1.pop(0))
        else:
            merged.append(l2.pop(0))

    while l1:
        merged.append(l1.pop(0))

    while l2:
        merged.append(l2.pop(0))
    return merged


a = merge_sort([5,4,3,2,1,10,9,8])
print(a)