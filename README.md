# TP final Bio informatica 2025 S1

Este software permite obetener los valores experimentaless de Kd, Ki e IC50 asociados a la estructura del codigo PDB suministrado

Output del programa:

- Resolución de la estructura
- Año de publicación
- Nombre y código del ligando
- Valores disponibles de Kd, Ki, IC50 (con unidad)
- Fuente del dato (PDBbind, BindingDB, ChEMBL)
- ID de UniProt o ChEMBL si están disponibles


### Instalacion del proyecto:

Clonar el repositorio:
`git clone git@github.com:CardozoCasariegoLuciano/BioInf_TP_2025_S1.git`

Instalacion de dependencias, dentro de la carpeta clonada:
`conda env create -f environment.yml`

Activar el entorno:
`conda activate TP_final`

Correr el programa:
`python -m main [PDBs] [OPTIONS]`

### Ejemplos

solo un PDB: `python -m main 1EES`

multiples PDBs: `python -m main 1EES 1TLD 4HHB`

archivo con PDBs `python -m main --pdb-file [PATH]`

filtrado por afinidad: `python -m main 1EES --filters Ki` | `python -m main 1EES -f Ki -f Kd`

filtrando por ligandos: `python -m main 1TLD --ligands 13939` | `python -m main 1TLD -l 13940 -l 13941 `

archivo con ligandos `python -m main --ligands-file [PATH]`

_Los archivos ignoran los comentarios con `#`_

### Tests
Para correr los tests, ejecutar el comando `pytests -v`
