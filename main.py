from src.CLI import process_data

if __name__ == "__main__":
    process_data()

    #TODO Consultar a las distintas bases de datos los datos buscados
    #TODO La salida tiene que ser en formato JSON
    #TODO Hacer la wiki de github
    #TODO hacer bien detallado el readme
    #TODO gregar los tests


# Salidas esperadas
#
# El paquete deberá brindar como salida un JSON, con la información correspondiente a cada una de las proteínas que interactúan con
# la PDB administrada como input. Las salidas deberán estar organizadas en un directorio. Y la herramienta debe resolver la instalación
# y descarga de recursos por sí misma. Los datos a contener en la salida deben incluir:
# - Resolución de la estructura
# - Año de publicación
# - Nombre y código del ligando
# - Valores disponibles de Kd, Ki, IC50 (con unidad)
# - Fuente del dato (PDBbind, BindingDB, ChEMBL)
# - ID de UniProt o ChEMBL si están disponibles
