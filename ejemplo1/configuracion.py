from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
#el echo se pone para saber en que proceso va
engine = create_engine('sqlite:///demobase.db', echo=True)

# mysql
# pip install mysql-connector-python
# engine = create_engine("mysql+mysqlconnector://user:pass@localhost:3306/demo100", echo=True)

# postgres
# sudo apt install libpq-dev (es un comando de intalacion, se esta instalando todo el programa en el S.O)
# pip install psycopg2
# engine = create_engine("postgresql+psycopg2://user:pass@localhost:5432/demo100", echo=True)


