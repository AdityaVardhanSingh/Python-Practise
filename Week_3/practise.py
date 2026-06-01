nums = [1,2]
nums.append(3)
print(nums)

nums = [1,2]
num2 = [2,4,6]
nums.append(num2)
print(nums)
"""it is making list in inside the original list
Example
[1, 2, 3]
[1, 2, [2, 4, 6]]"""

#Extend

var1 =[1,2]
var2= [4,2,8]
var1.extend(var2)
print(var1)
"""
[1, 2, 4, 2, 8]
"""
#Insert

var3 =[10,20,30]
var3.insert(2, 40)
print(var3)
#[10, 20, 40, 30]

#Remove

var4 =[10,20,30,40]
var4.remove(20)
print(var4)

#pop

var5 =[1,2,3,4,5]
var5.pop(3)
print(var5)

#Clear

var6 =[1,2,4,5,6]
var6.clear()
print(var6)

#Reverse

var7= [1,2,3,4,5,6]
var7.reverse()
print(var7)


## Tuple