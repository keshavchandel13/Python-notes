import itertools

def generate_permutations(numbers):
    """Generate all possible permutations of the given numbers."""
    permutations = list(itertools.permutations(numbers))
    return permutations

def print_permutations(permutations):
    """Print permutations in a simple format with four columns."""
    for i, perm in enumerate(permutations):
        print(perm, end='\t')
        if (i + 1) % 4 == 0:
            print()
    if len(permutations) % 4 != 0:
        print()

def calculate_mean(permutations):
    """Calculate the mean of all the numbers in all permutations."""
    total_sum = 0
    total_count = 0
    
    for perm in permutations:
        total_sum += sum(perm)
        total_count += len(perm)
    
    return total_sum / total_count

def main():
    # Take input from user
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    permutations = generate_permutations(numbers)

  
    print("Permutations of the input numbers:")
    print_permutations(permutations)

    # Calculate and print the mean
    mean_value = calculate_mean(permutations)
    print(f"Mean value of all permutations: {mean_value:.2f}")

if __name__ == "__main__":
    main()