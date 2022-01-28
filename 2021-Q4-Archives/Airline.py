'''Airline Restrictions'''

T= int(input())

for i in range(0,T):
    A,B,C,D,E=map(int,input().split())

    if A+B<=D and C<=E:
        print("YES")
        continue
    elif B+C<=D and A<=E:
        print("YES")
        continue
    elif A+C <=D and B<=E:
        print("YES") 
        continue
    else:
        print("NO")