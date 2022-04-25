# Lista de los primeros 10 números al cuadrado 

# Ejemplo Lista
# super_list = [
#       {"firstname": "Carolina", "lastname": "Muñoz" } ] 

def run():
    
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # squares = []
    # for i in range(1, 101):
    #     if (i % 3 == 0 ):
    #         squares.append(i**2)
     
    print (squares)

if __name__ == "__main__":
    run()