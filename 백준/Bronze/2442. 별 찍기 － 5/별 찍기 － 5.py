def star_tree(n):
    for i in range(n):
        # 왼쪽 공백
        print(" " * (n - i - 1), end="")
        # 왼쪽 별
        print("*" * (i + 1), end="")
        # 오른쪽 별
        print("*" * i)
        
# 입력을 받습니다
n = int(input().strip())
star_tree(n)