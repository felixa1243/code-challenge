for i in range(1,4):
    for j in range(1,6):
        print(j,end="")
    print()
    for k in range(5,0,-1):
        print(k,end = "")
    print()
#output
#1 2 3 4 5
#5 4 3 2 1
#1 2 3 4 5
#5 4 3 2 1
#1 2 3 4 5
#5 4 3 2 1
#It will print numbers 1-5 in four rows, and then print numbers 5-1 in four rows. Each inner loop iteration will print a number, and if the inner loop completed the outer loop will print new line before printing numbers 5-1 in descending order, and again a new line after that.

#The outer for loop iterates 3 times, on each iteration the inner for loop iterates 5 times and prints numbers 1-5, then the second inner for loop iterates 5 times, but in reverse order and prints the numbers 5-1 and goes to the next outer loop iteratio
