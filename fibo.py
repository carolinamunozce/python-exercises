
def fibo(num) :
    
    if num == 1:
        return 1
    elif num == 0:
        return 0
    elif num < 0:
        raise Exception ("Se rompio")
    return fibo(num - 1) + fibo(num - 2)

res = fibo(6)
print(res)
print (f'fibo({6}) == {res}') #0, 1, 1, 2, 3, 5, 6, 7, 8, 9