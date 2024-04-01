def max_activities(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by finish time
    selected = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] >= selected[-1][1]:  # If start time is after the previous activity finishes
            selected.append(interval)

    return selected

# Example intervals
intervals = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13),(12,14)]

result = max_activities(intervals)
print(result)
