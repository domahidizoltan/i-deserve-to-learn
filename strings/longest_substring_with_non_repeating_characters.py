# http://www.ideserve.co.in/learn/longest-substring-with-non-repeating-characters


def find_longest_non_repeating_substring(string):
    max_substring = ""
    max_substring_length = len(max_substring)

    for current_index, _ in enumerate(string):
        current_substring = get_substring_from(string, current_index)

        if is_longer_with_no_duplicates(current_substring, max_substring_length):
            max_substring = current_substring
            max_substring_length = len(max_substring)

    return max_substring


def get_substring_from(string, starting_index):
    char = string[starting_index]
    next_index = string.find(char, starting_index + 1)
    next_index = None if next_index == -1 else next_index
    return ''.join(string[starting_index:next_index])


def is_longer_with_no_duplicates(current_substring, max_substring_length):
    current_length = len(current_substring)
    return len(set(current_substring)) == current_length and max_substring_length < current_length


if __name__ == '__main__':
    long_string = "ABCDABDEFGCABD"
    substring = find_longest_non_repeating_substring(long_string)
    print("{} is the longest substring in {} with non-repeating characters.".format(substring, long_string))
