from clases import Estudiante , MongoDB
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("20161000992", "Joel", "almendarez", "25", "joel.almendares@unah.hn")
    estudiante.GuardarEstudiante()
    estudiante.ActualizarEstudiante()
    
if __name__ == '__main__':
    load_dotenv()
    main()