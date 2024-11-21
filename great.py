name = input("enter your name:")
marks = int(input("enter your marks : "))
if(marks>=90):
    print(f"A grade")
elif(80<=marks<=89):
    print(f"B grade")
elif(70<=marks<=79):
    print(f"C grade")
elif(60<=marks<=69):
    print(f" D grade")
else:
    grade = "Fail"
    print(grade)