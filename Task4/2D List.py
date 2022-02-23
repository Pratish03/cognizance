r1=['Name','Roll no','Marks']
l=[r1]
n=int(input("Enter how many records you want to add:"))
for i in range(n):
    print()
    print('Record number',i+1)
    print()
    d1=input("Enter Rollno:")
    d2=input("Enter name:")
    d3=input("Enter Marks:")
    r2=[d1,d2,d3]
    l.append(r2)
for i in l:
    if i[0]=='Roll no':
        print(i[0]+'   '+i[1]+'   '+i[2])
    else:
        print(3*' '+i[0]+3*'  '+i[1]+3*'  '+i[2])


if len(l)<3:
    print("The no of record is less than 2")
else:
    print("Second record/row")
    print(l[2][0]+'  '+l[2][1]+'  '+l[2][2])