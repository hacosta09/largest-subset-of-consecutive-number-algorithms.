
def find_longest_consecutive_sequence(nums):
    """
    Find the longest sequence of consecutive numbers in an unsorted list.
    :param nums: List of integers
    :return: List of integers representing the longest consecutive sequence
    """
    num_set = set(nums)  # Use a set for O(1) lookups
    longest_sequence = []
    links = {}

    for num in nums:
        # Only start building sequences from numbers that are the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = [current_num]

            # Build the sequence and the links
            while current_num + 1 in num_set:
                links[current_num] = current_num + 1
                current_num += 1
                current_sequence.append(current_num)

            # Update the longest sequence if the current is longer
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence

    # Print the links (optional)
    print("Number links (number -> next consecutive number):")
    for key in links:
        print(f"{key} -> {links[key]}")

    return longest_sequence


if __name__ == "__main__":
    # Sample input
    nums = [1, 3, 8, 14, 4, 10, 2, 11]

    # Find and print the longest consecutive sequence
    longest_sequence = find_longest_consecutive_sequence(nums)
    print("\nLongest consecutive sequence:")
    print(longest_sequence)
