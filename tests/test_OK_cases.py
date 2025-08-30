from src.API import create_output_from_APIs
from unittest.mock import patch
from pathlib import Path

def test_001_output_created_OK_Only_PDBs(capsys):
    output = Path("output/PDB_1EES.json")
    try:
        with patch("requests.get") as mock:
            mock.return_value.status_code = 200
            mock.return_value.json.return_value = { }
            create_output_from_APIs(["1EES"], [],[])

            captured = capsys.readouterr()
            assert output.exists()
            assert "Archivo generado correctamente" in captured.out
    finally:
        if output.exists():
            output.unlink()

def test_002_output_created_OK_filter_by_Ki(capsys):
    output = Path("output/PDB_1EES.json")
    try:
        with patch("requests.get") as mock:
            mock.return_value.status_code = 200
            mock.return_value.json.return_value = {
                "getLindsByPDBsResponse":{
                    "affinities": [
                        {
                            "monomerid": "123123",
                            "affinity_type": "Ki"
                        },
                        {
                            "monomerid": "222222222",
                            "affinity_type": "Kd"
                        },
                    ]
                }
            }
            create_output_from_APIs(["1EES"], [],["Ki"])


            captured = capsys.readouterr()
            assert output.exists()
            assert "123123" in output.read_text()
            assert not "222222222" in output.read_text()
            assert "Archivo generado correctamente" in captured.out
    finally:
        if output.exists():
            output.unlink()


def test_003_output_created_OK_ligand_222(capsys):
    output = Path("output/PDB_1EES.json")
    try:
        with patch("requests.get") as mock:
            mock.return_value.status_code = 200
            mock.return_value.json.return_value = {
                "getLindsByPDBsResponse":{
                    "affinities": [
                        {
                            "monomerid": "123",
                            "affinity_type": "Ki"
                        },
                        {
                            "monomerid": '222',
                            "affinity_type": "Kd"
                        },
                    ]
                }
            }
            create_output_from_APIs(["1EES"], ["222"],[])

            captured = capsys.readouterr()
            assert output.exists()
            assert not "123" in output.read_text()
            assert "222" in output.read_text()
            assert "Archivo generado correctamente" in captured.out
    finally:
        if output.exists():
            output.unlink()
