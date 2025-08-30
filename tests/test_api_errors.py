import pytest
from unittest.mock import patch
from src.API import get_data_from_RCSB, get_data_from_bindingPDB

def test_001_API_RCSB_fail(capsys):
    with patch("requests.get") as mock:
        mock.return_value.status_code = 400
        with pytest.raises(SystemExit) as e:
            get_data_from_RCSB("1EES")
        captured = capsys.readouterr()

    assert e.value.code == 1
    assert "Error al obeneter la informacion\n" == captured.out

def test_002_API_bindingPDB_fail(capsys):
    with patch("requests.get") as mock:
        mock.return_value.status_code = 400
        with pytest.raises(SystemExit) as e:
            get_data_from_bindingPDB("1EES", [], [])
        captured = capsys.readouterr()

    assert e.value.code == 1
    assert "Error al obeneter la informacion\n" == captured.out


