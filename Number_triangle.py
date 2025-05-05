def triangle(rows):
    for i in range(1,rows+1):
        if i % 2 == 0:
            r=i//2
        else:
            r=i//2+1
        for j in range (rows - i):
            print(" ",end = '')
        for k in range(r):
            print(k+1,end=" ")
        for l in range(i//2):
            if i % 2 == 0:
                p=k-l+1
            else:
                p=k-l
            print(p,end=" ")
        print()
rows=int(input("Enter the number of rows : "))
triangle(rows)