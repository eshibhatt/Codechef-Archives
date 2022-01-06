T= int(input())

for i in range(0,T):
  N,M=map(int,input().split())
  if N%2==0:
    avRows=N/2
  else:
    avRows=(N+1)/2
  
  if M%2==0:
    seatsPerRow=M/2
  else:
    seatsPerRow=(M+1)/2
  
  print(int(seatsPerRow*avRows))
#print(seatsPerRow,avRows)