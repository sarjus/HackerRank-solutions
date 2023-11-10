def main():
    # Initialize a trie to store keywords using Aho-Corasick algorithm
    root = {}
    add_keywords_to_trie(root, str(1))

    # Set highest power of 2 in the trie to 2^800
    for i in range(2, 801):
        add_keywords_to_trie(root, str(2 ** i))

    results = []
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        string_input = input().strip()
        power_of_two_count = find_power_of_two_occurrences(root, string_input)
        results.append(str(power_of_two_count))

    # Print the results for all test cases
    print('\n'.join(results))

def add_keywords_to_trie(root, keyword):
    """
    Add keywords to the trie (Aho-Corasick tree).
    At the last letter of the keyword, set a new value 'p'
    to mark it as a power of 2.
    """
    node = root
    length = len(keyword)

    # Iterate through all characters in the keyword
    for i in range(length):
        char = keyword[i]

        if char in node:
            node = node[char]
        elif i < length - 1:
            # If not the last character, move to the next character
            node[char] = {}
            node = node[char]
        else:
            # If the last character, flag it as a power of two
            node[char] = {'p': ''}

def find_power_of_two_occurrences(root, input_string):
    """
    Traverse the trie to find occurrences of the value 'p'
    and increment the counter for each occurrence.
    """
    counter = 0
    length = len(input_string)

    # Iterate through each substring starting from different indices
    for i in range(length):
        node = root

        # Iterate through the substring starting from index i
        for j in range(i, length):
            char = input_string[j]

            if char in node:
                node = node[char]

                # Check if the current node represents a power of 2
                if 'p' in node:
                    counter += 1
            else:
                break

    return counter

if __name__ == '__main__':
    main()
