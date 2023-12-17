trie = {
    "o": {"n": {"e": "1"}},
    "t": {"w": {"o": "2"}, "h": {"r": {"e": {"e": "3"}}}},
    "f": {"i": {"v": {"e": "5"}}, "o": {"u": {"r": "4"}}},
    "s": {"e": {"v": {"e": {"n": "7"}}}, "i": {"x": "6"}},
    "e": {"i": {"g": {"h": {"t": "8"}}}},
    "n": {"i": {"n": {"e": "9"}}},
}


def get_word_digits(l, index=0, word="", traversal=trie, result=""):
    if index > len(l) - 1:
        return result
    char = l[index]
    if str.isdigit(char):
        return get_word_digits(l[index + 1 :], 0, "", trie, result + char)
    traversed = traversal.get(char)
    if not traversed:
        return get_word_digits(l[1:], 0, "", trie, result)
    if type(traversed) is str:
        return get_word_digits(l[1:], 0, "", trie, result + traversed)
    return get_word_digits(l, index + 1, word + char, traversed, result)


result = 0
for line in open("puzzle.txt").read().splitlines():
    digits = get_word_digits(line)
    # print(line, digits)

    if digits:
        result += int(digits[0] + digits[-1])

print(f"Day 1, Part 2: {result=}")
