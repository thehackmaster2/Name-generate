import random

# Inyuguti zisanzwe zikoreshwa mu mazina y'abakobwa bo mu Rwanda
ibice1 = ["A", "Be", "Chi", "Di", "E", "Fa", "Ga", "Ha", "I", "Je", "Ka", "La", "Ma", "Na", "O", "Pa", "Ra", "Sa", "Ta", "U", "Va", "Wa", "Ya", "Za"]
ibice2 = ["line", "nita", "rine", "senga", "lida", "tina", "nette", "cia", "rielle", "lise", "ra", "yine", "mara", "nise", "rene", "thia", "nda", "sha", "lyse", "gue", "nia", "sa", "ra", "vie"]

def rema_izina():
    """Irema izina rishya hifashishijwe ibice bitandukanye"""
    return random.choice(ibice1) + random.choice(ibice2)

# Kwerekana amazina 10 yaremwe
n = int(input("Injiza umubare w'amazina ushaka: "))
amazina_mashya = [rema_izina() for _ in range(n)]
print("Amazina yaremwe:", amazina_mashya)