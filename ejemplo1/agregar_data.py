from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo
# no se pone el id porque es autoincremental ya que es primary key
miSaludo = Saludo()
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
