T=int(input())

for i in range(0,T):
  S=input()
  N=len(S)


  if N==1:
    print("No")

  elif S.find('1')==N-1 or S.find('1')==-1:
    print("No")
  else:
    print("Yes")
