from click.testing import CliRunner
from src.CLI import process_data

def test_001_No_PDB_sended():
    runner = CliRunner()
    result = runner.invoke(process_data, [])
    assert result.exit_code == 1
    assert "No se enviaron codigos PDB" in result.output

def test_002_invalid_format_PDB():
    runner = CliRunner()
    result = runner.invoke(process_data, ["ASDASDAJSD"])
    assert result.exit_code == 1
    assert "Uno o mas codigos PDB ingresado no cumple el formato" in result.output

def test_003_file_Not_found():
    file_name = "nanana"
    runner = CliRunner()
    result = runner.invoke(process_data, ["--pdb-file",file_name])
    assert result.exit_code == 2
    assert "'" + file_name + "'" + ": No such file or directory" in result.output

def test_004_invalid_PDB_in_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("fake.txt", "w") as file:
            file.write("ASDASD")
        result = runner.invoke(process_data, ["--pdb-file", "fake.txt"])
    assert result.exit_code == 1
    assert "Uno o mas codigos PDB ingresado no cumple el formato" in result.output

def test_005_empty_PDB_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("fake.txt", "w") as file:
            file.write("")
        result = runner.invoke(process_data, ["--pdb-file", "fake.txt"])
    assert result.exit_code == 1
    assert "El archivo no contiene codigos que pueda leer" in result.output

def test_006_inbvalid_filters():
    wrong_filter = "WWWW"
    runner = CliRunner()
    result = runner.invoke(process_data, ["3ASB" ,"-f", wrong_filter])
    assert result.exit_code == 1
    assert "Filtro " + wrong_filter + " invalido. los permitidos son: Kd, Ki y IC50" in result.output
