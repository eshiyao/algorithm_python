result=[]

def mergelist(list1,list2):
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1[0])
            del list1[0]
        else:
            result.append(list2[0])
            del list2[0]
    if list1:
        result.extend(list1)
    if list2:
        result.extend(list2)
    print(result)
    return result

l1=[1,3,5,7,8,10]
l2=[2,5,6,9,11]
mergelist(l1,l2)
        
