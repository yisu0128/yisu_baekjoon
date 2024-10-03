# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import math

n, m = map(int, sys.stdin.readline().rstrip().split())
number = (0.07*n/(n+m))*100
print(f"{math.floor(number * 100) / 100:.2f}")
