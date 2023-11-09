num_test_cases = int(input())

for _ in range(num_test_cases):
    # Input for each test case: length of the string, parameters a and b, and the input string itself
    length, cost_a, cost_b = map(int, input().split(' '))
    input_string = input().strip()

    # Initialize variables
    char_index = 1
    min_cost = 0

    # Create a list to store the minimum cost for each character position
    min_cost_list = [float('inf')] * (length + 1)
    min_cost_list[0] = 0
    last_matching_index = 0

    # Iterate over the characters in the input string
    while char_index <= length:
        # Find the maximum substring that matches a prefix of the string
        substring_index = max(char_index, last_matching_index)
        while substring_index <= length and (input_string[char_index - 1:substring_index] in input_string[:char_index - 1]):
            substring_index += 1

        # Update the minimum cost based on the conditions
        if substring_index - 1 != char_index:
            min_cost_list[substring_index - 1] = min(min_cost_list[char_index - 1] + cost_b, min_cost_list[substring_index - 1])
            last_matching_index = substring_index

        min_cost_list[char_index] = min(min_cost_list[char_index - 1] + cost_a, min_cost_list[char_index])

        # Move to the next character
        char_index += 1

    # Print the minimum cost for the current test case
    print(min_cost_list[-1])
