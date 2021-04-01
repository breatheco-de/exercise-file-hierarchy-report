# Trabajar con el Sistema de Archivos del Computador

Otra estructura de datos muy utilizada en el mundo de la codificación son los árboles (trees), por ejemplo:

1. El sistema de archivos del computador es un árbol.
2. El DOM (Document Object Model) es un árbol.

En este caso, usaremos el concepto de árbol de jerarquía  para escanear y navegar a través de un grupo de archivos en un computador.


## 🌱  Cómo iniciar este proyecto

No clones este repositorio.

1. El primer paso para comenzar a codificar es clonar el [python boilerplate](https://github.com/4GeeksAcademy/flask-rest-hello) en tu compjutador local o con Gitpod.

a) Si usas Gitpod (recomendado)  puedes clonar el boilerplate [clic aquí](https://github.com/4GeeksAcademy/flask-rest-hello).

b) Si trabajas localmente, escribe el siguiente comando en tu terminal: 
```sh
git clone https://github.com/4GeeksAcademy/flask-rest-hello
```

2. Instala los paquetes de la dependencia
```sh
$ pipenv install --python 3
```

3. Ingresa a tu entorni virtual escribiendo: 

```sh
$ pipenv shell
```

4. Puedes ejecutar el proyecto escribiendo:

```sh
$ python src/app.py
```
5. También puedes ejecutar las pruebas o tests del proyecto:

```sh
$ python src/test.py
```

💡 Importante: Recuerda actualizar el `remote` del proyecto con el de tu repositorio usando `git remote set-url origin <your new url>`, y luego guardar tu código en tu nuevo repositorio usando `add`, `commit` y `push`.


# 📝 Instrucciones

Muestra el conjunto de archivos que están en la carpeta `data-files`, escribe un programa que cree un JSON file llamado report.json cuya salida sea el siguiente reporte:


```json
{
    "levels": 3,
    "total_files_found": 5,
    "files_found": ["file_one.csv", "file_two.json"],
    "file_extentions_found": ["csv", "json"],
    "total_folders_found": 3,
    "folders_found": ["folder_one","folder_tow"],
    "links_found": 12,
    "broken_links_found": 4,
}
```

Explicación del Reporte o informe:

| Propiedad  | Descripción |
| --------  | ----------- |
| levels    | Cantidad de conexiones entre el nodo superior y el nodo inferior |
| total_files_found | cuántos archivos se encontraron, las carpetas no cuentan |
| files_found | nombre de cada archivo encontrado, sin las carpetas |
| file_extentions_found | una lista sin repeticiones de las extensiones de los archivos que se encuentran dentro del árbol|
| total_folders_found | cantidad total de carpetas encontradas, los archivos no cuentan|
| Links found | Cuántas URLs se encontraron comenzando con http o https |
| broken_links_found | Cuántos links o enlaces se rompieron (tienes que usar el método GET y verificar 404) |

## 💡 Hint

1. Empieza por buscar en google `python obtener archivos en carpeta` o  `python get files in folder`.
2. Esta búsqueda también ayuda: `archivo python es un directorio` o `python file is directory` para verificar si el archivo es un directorio o no. 
3. Para buscar en google cómo encontrar links o enlaces dentro del contenido del archivo: `python encuentra todos los links en string` o `python find all links in string`
4. Obtener la extensión del nombre del archivo: `python obtener extensión del archivo`o `python get file extension`
