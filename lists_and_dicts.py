"""
Ejemplos de listas y diccionarios
"""


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Carolina", "lastname": "Muñoz" }
    
    super_list = [
        {"firstname": "Carolina", "lastname": "Muñoz" },
        {"firstname": "Claudio", "lastname": "Muñoz" },
        {"firstname": "Martina", "lastname": "Oblitas" },
        {"firstname": "Antonio", "lastname": "Muñoz" }  ]

    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]          
    
    }
    #for key, value in super_dict.items():
       #print(key, "-", value)

    for values in super_list:
         print (values["firstname"], "-" ,values ["lastname"])

if __name__ == '__main__':
    run()

