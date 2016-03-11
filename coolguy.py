# cool-guy
lowtemp1=0
hightemp2=0
alltemps=[]
for i in range(3):
    temp=float(input("please enter the baby temp"))
    alltemps.append(temp)
    if temp<=36:
        print("baby's temp is too low")
    elif temp>37.5:
        print("baby's temp is too high")
    else:
        print("baby's temp is ideal")


#to calculate highest and lowest.
    if temp>hightemp2:
        hightemp2=temp
if temp<hightemp2:
    lowtemp1=temp
    print("the highest temp was",hightemp2, "and the lowest temp was",lowtemp1)
    difference=hightemp2-lowtemp1
    print(difference)
    print(alltemps)
#task 3
if difference>=1:
    print("this baby's temp is over-normal")





