from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    my_aircraft = Aircraft(model)
    while True:
        user_input = input("Enter command (A for ascent, D for descent, X to exit): ")
        
        parts = user_input.split()
        command = parts[0].upper() 
        