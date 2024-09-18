
usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = '004'

try:
    print(usuarios[id_usuario])
except KeyError:
    print("La clave 004 no está en el diccionario. Añadiendo clave...")
    usuarios["004"] = "Ninguno"
    print(usuarios)

