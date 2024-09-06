inp1 = input("Enter Your Marks: ")
marks = int(inp1)

if marks > 90:
    print("A Grade")
elif marks > 80:
    print("B Grade")
elif marks > 70:
    print("C Grade")
elif marks > 60:
    print("D Grade")
else:
    print("F Grade")