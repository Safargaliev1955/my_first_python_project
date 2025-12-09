def decorator(func):
    print("before")
    func()
    print("after")

@property
def greeting():
    print("Hello, World!")



