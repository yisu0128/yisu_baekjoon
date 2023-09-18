T = int(input())
words = []
for i in range(T):
    word = input()
    word = word[0]+word[-1]
    words.append(word)

for i in range(T):
    print(words[i])
