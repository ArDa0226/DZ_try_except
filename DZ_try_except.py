
def add_everything(a, b):
    try:
        result = a + b
    except TypeError:
        if type(a) == int or float and type(b) == str:
            a = str(a)
            result = a + b
        elif type(a) == str and type(b) == int or float:
            b = str(b)
            result = a + b
    finally:
        print(result)



add_everything('fg', 76)
add_everything(45, 'gh')
add_everything(130.34, 'try')
add_everything('exc', 345.56)


