from os import environ
LOCAL = environ.get("LOCAL")

def local(func):
    def innerFunc(*args, **kwargs):
        if LOCAL: return func()
    return innerFunc

@local
def debug(*args):
    print(*args)
