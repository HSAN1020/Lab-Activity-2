def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    # If all numbers appear equally, no mode
    if len(modes) == len(freq):
        return 0
    return modes[0]  # Return the first mode found

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    try:
        numbers = [float(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    print("List:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()