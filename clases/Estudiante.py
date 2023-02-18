from clases.MongoDB import MongoDB


class Estudiante :
    
    def __init__(self, numCuenta, nombre, apellido, correoEstudiantil):
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
    #la base es para saber en que registro ir a editar, puse numero de cuenta porque son dijitos q no cambian osea son unicos
    # en comparacion con los nombres porque puede haber varios con el mismo  
    base = {"numCuenta": self.numCuenta}
    campos = {"$set": {"numCuenta": numCuenta, "nombre": nombre, "apellido": apellido, "correoEstudiantil": correoEstudiantil}}
    collection.update_one(base,campos)
    client.close()
    
    
