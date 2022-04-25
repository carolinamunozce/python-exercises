#Recibe un número como parametro y 
#muestra todos los divisores de ese número
def divisors(num):
    try:
        if num < 0 :
            raise ValueError("No se puede ingresar valores menores a 0")

        divisors = []
        for i in range (1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("Ingresa un número : "))
        print (divisors(num))
        print ("Termino el programa")
    except TypeError:
        print ("Solo debes ingresar números positivos")


if __name__ == '__main__':
    run()