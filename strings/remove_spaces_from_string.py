# http://www.ideserve.co.in/learn/remove-spaces-from-string


def remove_spaces(message):
    stripped = [c for c in message if c is not " "]
    return "".join(stripped)


if __name__ == "__main__":
    print("string without spaces: ", remove_spaces("  Hi, How are you?  "))
