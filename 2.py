 for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()
#This code uses nested for loops to generate a right triangle with 5 rows. The outer loop uses the range() function to iterate 5 times, and the inner loop uses the range() function to iterate i times.

#On each iteration of the outer loop, the inner loop is executed and the * character is printed i times, where i is the current value of the outer loop. The end="" argument is used to prevent the cursor from moving to the next line after each print statement, this way all the * characters are printed on the same line. The print() statement at the end of the inner loop causes the cursor to move to the next line after the inner loop completes.

#So, the output will be a right triangle shape with 5 rows and the number of * on each row is increasing from 1 to 5, like this:

#*
#**
#***
#****
#*****
