def lista_alumnos(num_alumnos):
    alumnos=[]
    for n in range(num_alumnos):
        alumno = {}
        
        alumno['Nombre'] = input('Ingrese el nombre completo')
        alumno['Nota1'] = float(input('Ingrese nota 1'))
        alumno['Nota2'] = float(input('Ingrese nota 2'))
        alumno['Nota3'] = float(input('Ingrese nota 3'))
        
        alumnos.append(alumno)
    return alumnos
num_alumnos = int(input('Introduce la cantidad de alumnos: '))