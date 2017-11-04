# http://www.ideserve.co.in/learn/group-all-anagrams-together-set-1


def group_by_anagrams(words):
    word_dict = dict()
    result = list()

    for word in words:
        key = ''.join(sorted(word))
        word_dict.setdefault(key, list()).append(word)

    for _, value in sorted(word_dict.items()):
        result.extend(sorted(value))

    return result


if __name__ == '__main__':
    words = ["abcd", "abc", "abce", "acd", "abdc"]
    print("Input array grouped by anagrams: ", group_by_anagrams(words))
