# Instalacion 

***
### 1.-Instalacion de dependencias a Ejecutar 
 * Crear entorno virtual, python -m venv venv
 * Venv\Scripts\activate
 * pip install Flask 
 * pip freeze > requirements.txt


### 2.- En Api coinmarket deber, deber obtener la API_KEY de la url https://coinmarketcap.com/api/
### 3.- Instalar sqlite3
### 4.- Crear base de datos con los siguientes parametros en sqlite3
***
Columna,Tipo
* id integer, clave primaria
* date Text (formato YYYY-MM-DD)
* time Text (formato HH:MM:SS.nnn)
* from_currency integer Foreign key a CRYPTOS
* form_quantity Real
* to_currency integer Foreign key a CRYPTOS
* to_quantity Real

### 5.- Crear un archivo config.py, donde dejaras tu API_KEY, SECRET KEY, ruta de la base de datos, SECRET_KEY 




