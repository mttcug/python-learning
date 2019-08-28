# caculate A + B

# twoNums = input('input two numbers with two spaces between them:')
# nums = twoNums.split()
# sum = int(nums[0]) + int(nums[1])
# print('sum:', sum)

line1 = input('input peopleHeight chairHeight appleNum:')
line2 = input('input appleNum appleHeight number in 10  -  1000:')

peopleHeight = line1.split()[0]
chairHeight = line1.split()[1]
appleNum = line1.split()[2]

sum = 0
maxHeight = int(peopleHeight) + int(chairHeight)
print('maxHeight:', maxHeight)
for x in line2.split():
    if int(x) <= maxHeight:
        print(x)
        sum = sum + 1

print(sum)


