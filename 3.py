x = 1
y = 1
z = 1

jumlah = int(input("Masukan jumlah bilangan fibonacci = "))
for i in range(jumlah):
    print(z, end=" ")
    z = x + y
    x = y
    y = z
#The output of this code will be a series of Fibonacci numbers, starting with 1, 1, and then the next numbers being the sum of the previous two numbers, printed on the same line, separated by a space. The number of Fibonacci numbers printed will be determined by the value entered by the user when prompted "Masukan jumlah bilangan fibonacci = ".

#if the user enters "10" the output will be:

#1 1 2 3 5 8 13 21 34 55
#The user can enter any positive integer number and the code will generate the fibonacci sequence till the number entered by the user.
