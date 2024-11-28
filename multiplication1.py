print("****************Multiplication Table************")
while True:
    n = int(input("Enter a number:"))
    if(n==0):
        print("Thank You!!!")
        break
    else:
        for i in range(1,11):
            ans = n*i
            print(f"{n} * {i} = {ans}")