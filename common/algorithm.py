def levenshtein_distance(word1, word2):
    word1_length = len(word1) + 1
    word2_length = len(word2) + 1

    if min(word1_length, word2_length) == 1:
        return max(word1_length, word2_length)

    distance_table = [[i+j for i in range(word1_length)] for j in range(word2_length)]

    for i in range(1, word1_length):
        for j in range(1, word2_length):
            cost = int(word1[i-1] != word2[j-1])
            above = distance_table[j-1][i] + 1
            left = distance_table[j][i-1] + 1
            diagonal = distance_table[j-1][i-1] + cost
            distance_table[j][i] = min(above, left, diagonal)

    return distance_table[j][i]


if __name__ == "__main__":
    pass
