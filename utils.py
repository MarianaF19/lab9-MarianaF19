# utils.py
from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    persona = Person(name)
    
    done = False
    while not done:
        acc_num = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))
        nueva_cuenta = BankAccount(acc_num, balance)
        persona.add_account(nueva_cuenta)
        
        respuesta = input("Are you done adding accounts? (yes/no):\n").lower()
        if respuesta == "yes":
            done = True
            
    return persona