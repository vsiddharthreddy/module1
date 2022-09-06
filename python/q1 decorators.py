'''task1 Question 1
Write a decorator function which will accept a integer as runtime argument and return a multiplied result from decorated function.
Decorated function will take 2 integer argument and return sum of the same.
Ex-
@multi(x) def abc(y,z): print(c)
where c is -(y+z)*x if x = 5, y = 2, z = 4, then output is- (2+4)*5 = 30
'here we are not using hardcoded values. we are taking three values from user'
'''

x,y,z = map(int,(input().split()))
print('x',x,'y',y,'z',z)
'using decorator function and passing arguements in decorator function as well as in decorated function'
def multi(num):
    'decorator function using inner function and wrapper function to take arguements and pass to decorated function'
    def _multiply(method):
        def _multiply_method(a, b):
            return method(a, b) * num

        return _multiply_method

    return _multiply

'creating the decorated function add which has access to decorated value nad returns also to decorator function when called'
@multi(x)
def add(a, b):
'''decorated function which is called in the inner function and returned to wrapper function for next step afer
summing . next step is multiplication'''
    return a + b
'just by calilng decorated function in print statement we call call decorator function and operations'
print(add(y, z))

