for i in range(int(input())):
    dsa,toc,dm=map(int,input().split())

    dsa2,toc2,dm2=map(int,input().split())

    dragon=dsa+toc+dm

    sloth=dsa2+toc2+dm2

    if sloth>dragon:
        print("Sloth")
    elif dragon>sloth:
        print("Dragon")
    elif sloth==dragon:
        if dsa>dsa2:
            print("Dragon")
        elif dsa2>dsa:
            print("Sloth")
        elif dsa==dsa2:
            if toc>toc2:
                print("Dragon")
            elif toc2>toc:
                print("Sloth")
            else:
                print("Tie")