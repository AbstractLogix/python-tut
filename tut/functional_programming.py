
# Functional programming method focuses on results, not the process
# Emphasis is on what is to be computed
# Data is immutable
# Functional programming Decompose the problem into `functions`
# It is built on the concept of mathematical functions which uses conditional expressions and recursion to do perform the calculation
# It does not support iteration like loop statements and conditional statements like If-Else
#
# Everything in python is an object.
# isinstance(x, object)
# id(x) and will return it's memory location
#
# pointer
a = 244
print("the number before change is", a)
print("the id of number before change is", id(a))
a = 344
print("the number after change is", a)
print("the id of number after change is", id(a))

# Immutable types in python
# Tuple
# Int
# Float
# Complex
# Stringfrozen set [note: immutable version of the set]
# Bytes

# Haskell Prelude

# Numeric functions
# NOTE overloading is used here to account for different numerical types
# I'm sure there's a better way TODO this

# add : Num a => a -> a -> a


def add(a: int, b: int):  # type: ignore
    return a + b


def add(a: float, b: float):  # type: ignore
    return a + b


def add(a, b):
    # one would assume that '+' would imply numeric type instead we get 'any'.
    return a + b
    # add('ok', ', Oscar') returns 'ok, Oscar'


# subtract :: Num a => a -> a -> a
def subtract(a: int, b: int):
    return a - b
# even :: Integral a => a -> Bool
# returns true if a is even

# odd :: Integral a => a -> Bool
# returns true if a is odd

# gcd :: Integral a => a -> a -> a
# greatest common divisor

# Misc functions

# id :: a -> a
# identity function
# NOTE this overrides built in id()

# const :: a -> b -> a
# const x y always evaluates to x, ignoring its second argument
