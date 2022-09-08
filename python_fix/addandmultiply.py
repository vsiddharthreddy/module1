'''task1 Question 1
Write a decorator function which will accept a integer as runtime argument and return a multiplied result from decorated function.
Decorated function will take 2 integer argument and return sum of the same.
Ex-
@multi(x) def abc(y,z): print(c)
where c is -(y+z)*x if x = 5, y = 2, z = 4, then output is- (2+4)*5 = 30
'here we are not using hardcoded values. we are taking three values from user'
'''
'line10 and 11 in miain method'

# taking three input values from user
print('please input three integer values')
x, y, z = map(int, (input().split()))


# defining a decorator function

def multi(z):
    print('inside multi func')

    def param_decofunc(func):
        print('inside param_decofunction ')

        def wrapper(*args, **kwargs):
            print('inside wrapper function ')
            sum1 = func(*args, **kwargs)
            # print('the sum of {} and {} is {}',format(x,y,sum))
            print('(x+y)*z = ', sum1 * z)

        return wrapper

    return param_decofunc


@multi(z)
def add_func(x, y):
    sum = x + y
    print('inside add_func')
    print(sum)
    return sum

def start():
    add_func(x,y)


if __name__ == "__main__":
    start()
