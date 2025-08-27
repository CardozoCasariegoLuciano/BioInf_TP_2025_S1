from io import TextIOWrapper
import click
import sys
import re
from .messages_manager import messages_manager

"""
bases de datos
Valida los args de entrada antes de iniciar con el llamado a las
"""
@click.command()
@click.argument("pdb", nargs=-1, type=str)
@click.option("--pdb-file", type=click.File("r") ,help="path del archivo contenedor de PBDs en texto plano, ignora comentarios con #")
@click.option("--ligands", "-l", multiple=True, help="ligandos, se aceptan multiples agregando el flag -l en cada uno")
@click.option("--ligands-file" , type=click.File("r"), help="path del archivo contenedor de los ligandos en texto plano, ignora comentarios con #")
@click.option("--filters", "-f", multiple=True, help="filtros a aplicar en la busqueda: Kd, Ki y/o IC50, cada uno separado por su flag -f. Por defecto los usa todos")
def process_data(pdb, pdb_file, ligands, ligands_file, filters):
    if pdb_file == None and len(pdb) == 0:
        messages_manager.Error_No_PDB_provide()
        sys.exit(1)

    PDBs = unify_and_validate_codes(list(set(pdb)),pdb_file, True)
    Ligands = unify_and_validate_codes(list(set(ligands)),ligands_file)
    Filter = validate_filters_or_exit(list(set(filters)))

    print("PDBs" ,PDBs)
    print("Ligandos" ,Ligands)
    print("filters", Filter)

    #TODO hacer los llamados a las distintas bases de datos


def unify_and_validate_codes(codes: list[str], file: TextIOWrapper , validate_PDB = False) -> list[str]:
    all_pdb = []

    if(codes):
        for pdb in codes:
            if validate_PDB:
                is_valid_PDB_or_exit(pdb)
            all_pdb.append(pdb)

    if(file):
        all_pdb.extend(get_codes_from_file(file, validate_PDB))

    return all_pdb


def get_codes_from_file(file: TextIOWrapper, is_PDB_file: bool) -> list[str]:
    code_list = []
    try:
        for line in file.readlines():
            line = line.strip()
            if line and not line.startswith("#"):
                code = line.split("#")[0].strip()
                if code:
                    if(is_PDB_file):
                        is_valid_PDB_or_exit(code)
                    code_list.append(code)
        if len(code_list) == 0:
            messages_manager.Error_Empty_file()
            sys.exit(1)
        return list(set(code_list))
    except Exception:
        messages_manager.Error_unexpected_error_at_read_file(file)
        sys.exit(1)


def is_valid_PDB_or_exit(pdb):
    pattern = r'^[1-9][a-zA-Z0-9]{3}$'
    is_valid = bool(re.match(pattern, pdb))
    if not is_valid :
        messages_manager.Error_invalid_PDB()
        sys.exit(1)


"""
Valida que los filtros sean validos.
Si no hay filtros en los argumentos los retorna a todos
"""
def validate_filters_or_exit(filters: list[str]):
    values = ["Kd", "Ki", "IC50"]

    if len(filters) > 0:
        for filter in filters:
            if not filter in values:
                messages_manager.Error_Filter_does_not_exist(filter)
                sys.exit(1)
        return filters
    else:
        return values

