def run():
   # squares = [i ** 2  for i in range (1, 6) ]
   my_list = [1, 2, 3, 4, 5]
   #squares = [i ** 2  for i in my_list ]
   squares = list(map(lambda x: x**2, my_list))

   print (squares)

if __name__=='__main__':
    run()