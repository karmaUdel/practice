def counting_sort(the_list, max_value):
    # List of 0's at indices 0...max_value
    num_counts = [0] * (max_value + 1)

    # Populate num_counts
    for item in the_list:
        num_counts[item] += 1

    # Populate the final sorted list
    sorted_list = []

    # For each item in num_counts
    for item, count in enumerate(num_counts):

        # For the number of times the item occurs
        for _ in xrange(count):

            # Add it to the sorted list
            sorted_list.append(item)

    return sorted_list