import tkinter as tk

# Datos de ejemplo
pokemons = [
    {"name": "Bulbasaur", "type": "Grass/Poison", "description": "Bulbasaur description."},
    {"name": "Charmander", "type": "Fire", "description": "Charmander description."}
    # ... Agrega más Pokémon aquí
]

# Función para mostrar los detalles del Pokémon
def show_pokemon_details(pokemon):
    name_var.set(pokemon["name"])
    type_var.set(f"Type: {pokemon['type']}")
    description_var.set(pokemon["description"])

# Crear ventana principal
root = tk.Tk()
root.title("Pokédex")

name_var = tk.StringVar()
type_var = tk.StringVar()
description_var = tk.StringVar()

# Widgets para mostrar información
name_label = tk.Label(root, textvariable=name_var, font=("Arial", 24))
name_label.pack()
type_label = tk.Label(root, textvariable=type_var, font=("Arial", 16))
type_label.pack()
description_label = tk.Label(root, textvariable=description_var, font=("Arial", 14))
description_label.pack()

# Botones para cada Pokémon
for pokemon in pokemons:
    button = tk.Button(root, text=pokemon["name"], command=lambda p=pokemon: show_pokemon_details(p))
    button.pack()

# Iniciar la aplicación
root.mainloop()
