import math

def my_decorato(func):
    def wrapper():
        print("before decorating")
        func()
        print("after decorating")

    return wrapper

@my_decorato
def say():
    print("Hi")

if __name__ == "__main__":
    say()