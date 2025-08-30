import json
import os
import sys
from typing import Dict
import requests
import click
from .messages_manager import messages_manager
from src.spinner import Spinner

def create_output_from_APIs(pdbs, ligands, filters):
    for pdb in pdbs:
        click.secho("Buscando informacion de PDB: " + pdb, bold=False)
        pdb_data = get_data_from_RCSB(pdb)

        spinner = Spinner("⏳ Buscando ligandos")
        spinner.start()
        pdb_ligands = get_data_from_bindingPDB(pdb, ligands, filters)
        spinner.stop()

        final_data = pdb_data | pdb_ligands
        file_name = create_output_file(pdb, final_data)
        click.secho("Archivo generado correctamente: " + file_name , fg="green", bold=False)

def get_data_from_RCSB (pdb) -> Dict:
    url = "https://data.rcsb.org/rest/v1/core/entry/" + pdb
    resp = requests.get(url)
    try:
        if(resp.status_code == 200):
            data = resp.json()

            year = data.get("citation", [{}])[0].get("year", "Year no find")

            resp = {
                "PDB": pdb,
                "Year": year,
                "Sources" : "RCSB, BindingPDB",
                "Uniprot id": None,
                "ChEMBL id": None
            }
            return resp
        else:
            messages_manager.Error_response_not_OK()
            sys.exit(1)
    except Exception as e:
        messages_manager.Error_response_not_OK(e)
        sys.exit(1)

def get_data_from_bindingPDB (pdb, input_ligands, input_filters) -> Dict[str, list]:
    url = "https://bindingdb.org/rest/getLigandsByPDBs?pdb=" + pdb + "&response=application/json"
    resp = requests.get(url)
    try:
        if(resp.status_code == 200):
            data = resp.json()

            ligands_data = data.get("getLindsByPDBsResponse", {}).get("affinities", {})
            filtered_ligands = []

            if not input_filters and not input_ligands:
                filtered_ligands = ligands_data
            else:
                for lig in ligands_data:
                    monomerid = lig.get("monomerid")
                    affinity_type = lig.get("affinity_type")

                    if input_ligands and monomerid in input_ligands:
                        filtered_ligands.append(lig)
                    if input_filters and affinity_type in input_filters:
                        filtered_ligands.append(lig)

            resp = {
                "ligands":filtered_ligands
            }
            return resp
        else:
            messages_manager.Error_response_not_OK()
            sys.exit(1)
    except Exception as e:
            messages_manager.Error_response_not_OK(e)
            sys.exit(1)

def create_output_file(pdb, data) -> str:
    os.makedirs("output", exist_ok=True)
    file_name = "output/PDB_" + pdb + ".json"
    with open(file_name, "w") as f:
      json.dump(data, f, indent=4)
    return file_name


