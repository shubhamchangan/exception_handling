a = 10
b = '0'
try: print(a/b)
except ZeroDivisionError:
    b = 2
    print(a/b)
except TypeError:
    try:
        print(int(a)/int(b))
    except:
        a = 30
        b = 4
        print(a/b)