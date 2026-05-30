marks_1 = int(input("Enter your 1 marks: "))
marks_2 = int(input("Enter your 2 marks: "))
marks_3 = int(input("Enter your 3 marks: "))

# for percantage

total_percentage = (100*(marks_1 + marks_2 + marks_3)/300) 
if(total_percentage>=40 and marks_1>=33 and marks_2>=33 and marks_3>=33):
    print("Good news! \nyou are passed. keep going.", total_percentage)
else:
    print("Good try! \nNow, try next year", total_percentage)