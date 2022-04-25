#Recibe un número como parametro y 
#muestra todos los divisores de ese número
def divisors(num):
    
        divisors = []
        divisors = [i for i in range (1, num + 1) if num % i == 0]
        return divisors
   

def run():
        num = input("Ingresa un número : ")
        assert num.isnumeric() and int(num) > 0, "Debes ingresar un número"
        print (divisors(int(num))) 
        print ("Termino el programa")



if __name__ == '__main__':
    run()