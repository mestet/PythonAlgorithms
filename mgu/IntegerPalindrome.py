num = int(input("Enter a number:"))
temp = num
rev = 0
while num > 0:
    print("num = " + str(num))
    dig = num % 10
    print("dig = " + str(dig))
    rev = rev * 10 + dig
    print("rev = " + str(rev))
    num = num // 10
if temp == rev:
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
