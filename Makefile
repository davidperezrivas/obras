freeze:
	pip freeze > requirements.txt


install:
	pip install -r requirements.txt
	
start:
	python app.py 

#Genera la carpeta de las migraciones
init:
	flask db init

#Trae los cambios
stamp:
	flask db stamp head

#Genera los archivos de cambios
migrate:
	flask db migrate

#actualiza la tabla de BD
migracion: stamp migrate
	flask db upgrade

virtual: 
	python -m venv venv


