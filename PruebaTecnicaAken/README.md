📝 Traducción completa de JSON a Inglés
Este script permite traducir todo el contenido de un archivo JSON al inglés, incluyendo:

✅ Claves (keys)

✅ Valores (values)

✅ Objetos y listas anidadas

Utiliza la librería deep-translator que es compatible con Python 3.13 y versiones anteriores.

📦 Requisitos
Python 3.7 o superior

Instalar deep-translator: pip install deep-translator

⚙️ Uso
Coloca tu archivo Prueba_Junior.json en la misma carpeta del script.

Ejecuta el script: python main.py

🧠 ¿Qué hace el script?

Carga el JSON original.

Recorre recursivamente cada clave y cada valor.

Traduce todo texto al inglés usando Google Translate vía deep-translator.

Mantiene la estructura original del JSON.

Guarda el resultado traducido en un nuevo archivo.

🚨 Notas

El script ignora y mantiene intactos los valores que no son texto (números, booleanos, null, etc.).

En caso de error de red o límite de traducciones, se mostrará un mensaje por consola y el valor original se conservará.

