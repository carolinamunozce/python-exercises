"""
Diccionario con list comprehension
"""

diccionary = {
        'Carolina': 36,
        'Martina':11,
        'Luis': 71,
        'Claudio':39 
    }
    

list_dic = {dic:valores for dic,valores in diccionary.items() if valores > 15}
print (list_dic)
    