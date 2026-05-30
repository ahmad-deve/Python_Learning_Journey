def student_first_process_step(func):
    def wrapper(*agr,**kwagr):
        print("first ! you take the information !")
        func(*agr,**kwagr)
    return wrapper
def student_second_process_step(func):
    def wrapper(*agr,**kwagr):
        print("After! check you are eligable for this program or not.")
        func(*agr,**kwagr)
    return wrapper
def student_final_process_Step(func):
    def wrapper(*agr,**kwagr):
        print("Apply for this progam! ")
        func(*agr,**kwagr)
    return wrapper
@student_first_process_step
@student_second_process_step
@student_final_process_Step
def student_info(name_college):
    print(f"Now! you successfully take Admission in our {name_college}s.")
input_name = input("Enter your college name: ")
student_info(input_name)