import json
from deep_translator import GoogleTranslator

# Crear una instancia del traductor
translator = GoogleTranslator(source='auto', target='en')

# Función recursiva para traducir claves y valores
def traducir_todo(data):
    if isinstance(data, dict):
        nuevo_dict = {}
        for clave, valor in data.items():
            clave_traducida = traducir_texto(clave)
            nuevo_dict[clave_traducida] = traducir_todo(valor)
        return nuevo_dict
    elif isinstance(data, list):
        return [traducir_todo(item) for item in data]
    elif isinstance(data, str):
        return traducir_texto(data)
    else:
        return data  # Números, booleanos, None, etc.

# Función para traducir texto con manejo de errores
def traducir_texto(texto):
    try:
        return translator.translate(texto)
    except Exception as e:
        print(f"Error al traducir '{texto}': {e}")
        return texto

# Leer el archivo original
with open('Prueba_Junior.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traducir todo
data_traducida = traducir_todo(data)

# Guardar el archivo traducido
with open('archivo_traducido.json', 'w', encoding='utf-8') as f:
    json.dump(data_traducida, f, ensure_ascii=False, indent=2)

print("✅ JSON traducido completamente, incluyendo claves y valores.")
