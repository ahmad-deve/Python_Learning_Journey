def about_essay(fun):
    def wrapper(name,sumester,earning_status):
        print(f"My name is {name}.He is in {sumester} of software engineer, He is {earning_status}.")
        fun(name,sumester,earning_status)
        print("after end")
    return wrapper
@about_essay
def meet(name,sumester,earning_status):
    print(f"Greeting:", {name})
meet("Ahmad", "first","not_earning")