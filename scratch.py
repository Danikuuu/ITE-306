num = 5
num2 = 3

sum = (num + num2)
difference = (num - num2)
product = (num * num2)
quotient = (num / num2)

print("sum is : " + str(sum))
print("difference is : " + str(difference))
print("product is : " + str(product))
print("quotient is : " + str(quotient))

ans = [str(sum), str(difference), str(product), str(quotient)]
print(ans)


l = '\n'.join(ans)
print(l)

num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))

sum1 = float((num3+num2))
print("The sum of " + str(num3) + " and " + str(num4) + " is " + str(sum1))
