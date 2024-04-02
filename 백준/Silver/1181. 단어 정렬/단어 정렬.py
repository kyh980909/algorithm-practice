N = int(input())

words = set()
words_len = set()

for _ in range(N):
    word = input()
    words.add(word)
    words_len.add(len(word))

words = list(words)
words = sorted(words)
words_len = list(words_len)
words_len = sorted(words_len)

solve = []

for length in words_len:
    i = 0
    while len(words) > i:
        if length == len(words[i]):
            solve.append(words[i])
            del words[i]
        else:
            i += 1

for word in solve:
    print(word)