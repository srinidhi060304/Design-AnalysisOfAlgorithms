class Item:
    def __init__(self, benefit, weight):
        self.benefit = benefit
        self.weight = weight
        self.value_per_unit = benefit / weight

def fractional_knapsack(items, capacity):
    # Sort items by value per unit weight in descending order
    items.sort(key=lambda x: x.value_per_unit, reverse=True)
    
    total_value = 0
    sack = []

    for item in items:
        if capacity >= item.weight:
            # If the item can be fully added to the sack
            sack.append((item.benefit, item.weight))
            total_value += item.benefit
            capacity -= item.weight
        else:
            # If only a fraction of the item can be added
            fraction = capacity / item.weight
            sack.append((item.benefit * fraction, item.weight * fraction))
            total_value += item.benefit * fraction
            break  # Sack is full

    return sack, total_value

# Example usage
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
optimal_solution, optimal_value = fractional_knapsack(items, capacity)
print("Optimal solution:")
for benefit, weight in optimal_solution:
    print(f"Benefit: {benefit}, Weight: {weight}")
print("Total value:", optimal_value)
