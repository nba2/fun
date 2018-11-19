"""Methods having to do with decoration."""

def tag(f):
    """Tag a function definition."""
    f.secret = 42
    return f

def count(f):
    """A decorator for counting function calls."""
    def wrapper(*args):
        wrapper.counter += 1
        return f(*args)
    wrapper.counter = 0
    return wrapper

def memoize(f):
    def wrapper(*args):
        if args not in wrapper.cache:
                wrapper.cache[args] = f(*args)
        return wrapper.cache[args]
    wrapper.cache = dict()
    return wrapper

@count
@memoize
def fibo(n):
    """Compute the nth Fibonacci number."""
    return n if n < 2 else fibo(n-1) + fibo(n-2)

def nope(f):
    def zippo(*args):
        print("You wish")
    return zippo

@nope
def cube(n):
    return n**3
