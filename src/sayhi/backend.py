import howto

def say(text, animal):
    print(text)
    add_bubble(animal)

def add_bubble(animal):
    animal_func = getattr(howto.animals, animal, None)
    if animal_func:
        print(animal_func())
    else:
        print(f"Animal '{animal}' not found :()")
