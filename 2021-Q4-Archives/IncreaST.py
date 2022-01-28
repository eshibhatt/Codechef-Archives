'''Lexicographically minimum string rotation'''

T=int(input())

def minLexRotation(str_) :
    n = len(str_)
    arr = [0] * n
    concat = str_ + str_
    for i in range(n) :
        arr[i] = concat[i : n + i]
    arr.sort()
    return arr[0]

for i in range(0,T):
  strIN=input()
  print(minLexRotation(strIN))