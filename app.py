from clases import Estudiante , MongoDB
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("201610654942", "Joel", "Almendarez", "25", "joel.almendares@unah.hn")
    estudiante.GuardarEstudiante()

    #No pude hacer las pruebas para saber si realmente funciona porque mi compu instalo el pymongo y el python-dotenv
    # pero nunca los detectaba, asi que puede que tenga errores 
    estudiante.nombre = 'Joel Antonio'
    estudiante.apellido = 'ALmendarez Sosa'
    estudiante.ActualizarEstudiante()

    
if __name__ == '__main__':
    load_dotenv()
    main()
