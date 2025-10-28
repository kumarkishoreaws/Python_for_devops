# "and" gives True only if both sides are True
# or gives True if at least one condition is True.


a = 5
b = 6
c= 5
x = False
y = False
total =10 

sum = a + b
diff = a - b
pro = a * b
div = a / b 


print ("sum of a and b is : " + str(sum))
print ("difference of a and b is : " + str(diff))
print ("product of a and b is : " + str(pro))
print ("sum of a and b is : " + str(div))

greater = a > b
less = a < b
g_e = a >= b
l_e = a <= b
e_e = a == b
n_e = a != b

print ("a greater b is : " + str(greater))
print ("a less b is : " + str(less))
print ("a greater than or equal to b is : " + str(g_e))
print ("a less than or equal to b is : " + str(l_e))
print ("a equals to b : " + str(e_e))
print ("a is not equal to b : " + str(n_e))

opr_and = x and y
opr_or = x or y
opr_not =  not y

print(opr_and)
print(opr_or)
print(opr_not)

total += total
total -= 5
total *= total
total /= 26

print("Final total value is : " + str(total))


is_operator = a is c
print("a is c : " + str(is_operator))