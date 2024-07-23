count = 0 
word = str(input())

for i in range(0, len(word)):
    if count < 9:
        print(word[i], end ='')
        count+=1
    elif count == 9:
        print(word[i])
        count = 0