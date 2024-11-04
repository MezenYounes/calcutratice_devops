def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y
    
def Multiplication(x,y):
    return x * y
def Division(x, y):
    if y==0:
    return "Error :division par zero"
     return x / y

def calculatrice():
    print("Sélectionnez l'opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Entrez le numéro de l'opération (1/2/3/4): ")

    if choix in ['1', '2', '3', '4']:
        try:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
            return

        if choix == '1':
            print(f"{a} + {b} = {addition(a, b)}")
        elif choix == '2':
            print(f"{a} - {b} = {soustraction(a, b)}")
        elif choix == '3':
            print(f"{a} * {b} = {multiplication(a, b)}")
        elif choix == '4':
            print(f"{a} / {b} = {division(a, b)}")
    else:
        print("Choix invalide")
        
if __name__ == "__main__":
    calculatrice()
