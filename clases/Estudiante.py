from clases.MongoDB import MongoDB


class Estudiante :
    
    def __init__(self, numCuenta, nombre, apellido,correoEstudiantil):
        self.numCuenta = numCuenta
        self.nombre = nombre
        self.apellido = apellido
        self.correoEstudiantil = correoEstudiantil
        self.__collection = "estudiante"
        
def GuardarEstudiante(self):
    client, db = MongoDB.getDB()
    collection = db[self.__collection]
    collection.insert_one(self.__dict__)
    client.close()

def ActualizarEstudiante(self):
    client, db = MongoDB.getDB()
    collection = db[self.__collection]
    collection.insert_one(self.__dict__)
    client.close()
    
    
