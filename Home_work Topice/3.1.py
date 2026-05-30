def outer(ahmad):
    def inner():
        print("this is the before: ")
        ahmad()
        print("After print")
    return inner
@outer
def say_hello():
    print("Hello")
say_hello()