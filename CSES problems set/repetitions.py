def find_repetitions(s):
    max_repetitions = 1
    curr_repetitions = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_repetitions += 1
            max_repetitions = max(max_repetitions, curr_repetitions)
        else:
            curr_repetitions = 1

    return max_repetitions

s = input()
print(find_repetitions(s))

