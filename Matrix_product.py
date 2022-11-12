# Matrix Product
# Using list comprehension + loop

def prob(val):
    res=1
    for ele in val:
        res*=ele # res=res*ele
        #print(res,ele)
    return res
# initializing list
test_list=([1 , 4, 5],[5,6],[1,4,7])

# printing original list
print("enter real number "+str(test_list))

# using list comprehension + loop
# Matrix Product
res= prob(ele for sub in test_list for ele in sub)
print("the total element product in list is =",str(res))