import click

class ErrorMessages:
    def Error_invalid_PDB(self):
        click.secho("Uno o mas codigos PDB ingresado no cumple el formato", fg="red", bold=True)

    def Error_file_not_found(self, file_path):
        click.secho("No se encontro el archivo " + file_path , fg="red", bold=True)

    def Error_unexpected_error_at_read_file(self, file_path):
        click.secho("Ocurrio un error al intentar leer el archivo " + file_path, fg="red", bold=True)

    def Error_Filter_does_not_exist(self, filter):
        click.secho("Filtro " + filter + " invalido. los permitidos son: Kd, Ki y IC50", fg="red", bold=True)

messages_manager = ErrorMessages()
