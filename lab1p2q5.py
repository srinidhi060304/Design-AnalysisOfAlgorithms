def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # If there is overlap
            merged[-1] = (merged[-1][0], max(interval[1], merged[-1][1]))
        else:
            merged.append(interval)

    return merged

# Example intervals
intervals = [(1,4),(2,5),(7,8),(6,9)]

result = merge_intervals(intervals)
print(result)
