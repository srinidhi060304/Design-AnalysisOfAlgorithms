import heapq

def merge_sorted_lists(lists):
    merged_list = []
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, lst_idx, idx = heapq.heappop(heap)
        merged_list.append(val)
        if idx + 1 < len(lists[lst_idx]):
            next_val = lists[lst_idx][idx + 1]
            heapq.heappush(heap, (next_val, lst_idx, idx + 1))

    return merged_list

# Example lists
lists = [
    [10,20,30,40],
    [15,25,35],
    [27,29,37,48,93],
    [32,33]
]

result = merge_sorted_lists(lists)
print(result)
