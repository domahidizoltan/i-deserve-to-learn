# http://www.ideserve.co.in/learn/word-break-problem

from collections import namedtuple

Word = namedtuple('Word', ['start', 'end', 'word'])


def words_are_connected(words, key, limit):
    if key == limit:
        return True

    if key in words.keys():
        for word in words[key]:
            are_connected = words_are_connected(words, word.end, limit)
            if are_connected:
                return True

    return False


def brake_word(msg, dictionary):
    words = dict()
    existing_words = [word for word in dictionary if word in msg]
    for word in existing_words:
        idx = msg.find(word)
        if idx not in words.keys():
            words[idx] = list()
        words[idx].append(Word(idx, idx + len(word), word))

    return words_are_connected(words, 0, len(msg))


if __name__ == "__main__":
    dictionary = ["arrays", "dynamic", "heaps", "IDeserve", "learn", "learning", "linked", "list", "platform",
                  "programming", "stacks", "trees"]
    msg = "IDeservelearningplatform"
    print("string could be broken into valid words: ", brake_word(msg, dictionary))
