import click

class ErrorMessages:
    def Error_No_PDB_provide(self):
        click.secho("No se enviaron codigos PDB", fg="red", bold=True)

    def Error_invalid_PDB(self):
        click.secho("Uno o mas codigos PDB ingresado no cumple el formato", fg="red", bold=True)

    def Error_unexpected_error_at_read_file(self, file_path):
        click.secho("Ocurrio un error al intentar leer el archivo " + file_path, fg="red", bold=True)

    def Error_Filter_does_not_exist(self, filter):
        click.secho("Filtro " + filter + " invalido. los permitidos son: Kd, Ki y IC50", fg="red", bold=True)

    def Error_Empty_file(self):
        click.secho("El archivo no contiene codigos que pueda leer", fg="red", bold=True)

    def Error_response_not_OK(self, e=None):
        click.secho("Error al obeneter la informacion", fg="red", bold=True)
        if(e):
            click.secho(e, bold=False)


messages_manager = ErrorMessages()
