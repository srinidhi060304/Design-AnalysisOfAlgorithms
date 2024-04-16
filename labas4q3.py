def minimize_sum_of_products(array_one, array_two):
    array_one.sort()  # Sort array_one in non-decreasing order
    array_two.sort(reverse=True)  # Sort array_two in non-increasing order

    min_sum = sum(array_one[i] * array_two[i] for i in range(len(array_one)))
    return min_sum

# Example usage
array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
minimized_sum = minimize_sum_of_products(array_one, array_two)
print("Minimized sum of products:", minimized_sum)
