import json
import os
from typing import Dict
import requests

URLS_1 = "https://data.rcsb.org/rest/v1/core/entry/{pdb_id}" # Informacion general del PDB
URLS_2 = "https://bindingdb.org/rest/getLigandsByPDBs?pdb=1MQ8&response=application/json" #Informacion de los ligandos
URLS_3 = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=8145218&retmode=json" #El id lo saco del URLS_2

#TODO manejar los mensajes miestras busca
#TODO Tests
#TODO mostrar todos los ligandos del URL2 que indiquen los filtros
#TODO Mostrar solo los ligandos que se indiquen en el input
#TODO crear el archivo output

def create_output_from_APIs(pdbs, ligands, filters):
    for pdb in pdbs:
        pdb_data =get_data_from_RCSB(pdb)
        pdb_ligands =get_data_from_bindingPDB(pdb)
        final_data = pdb_data | pdb_ligands
        create_output_file(pdb, final_data)


def get_data_from_RCSB (pdb) -> Dict:
    url = "https://data.rcsb.org/rest/v1/core/entry/" + pdb
    resp = requests.get(url)
    try:
        if(resp.status_code == 200):
            data = resp.json()

            resp = {
                "PDB": pdb,
                "Year": data["citation"][0].get("year"),
                "Sources" : "RCSB, BindingPDB",
                "Uniprot id": None,
                "ChEMBL id": None
            }
            return resp
        else:
            print("rompe antes ")
            return {}
    except Exception as e:
        print("error", e)
        return {}

def get_data_from_bindingPDB (pdb) -> Dict[str,str]:
    url = "https://bindingdb.org/rest/getLigandsByPDBs?pdb=" + pdb + "&response=application/json"
    resp = requests.get(url)
    try:
        if(resp.status_code == 200):
            data = resp.json()

            resp = {
                "ligands": data.get("getLindsByPDBsResponse").get("affinities")
            }
            return resp
        else:
            print("rompe antes ")
            return {}
    except Exception as e:
            print("error", e)
            return {}

def create_output_file(pdb, data):
    os.makedirs("output", exist_ok=True)
    with open("output/PDB_" + pdb + ".json", "w") as f:
      json.dump(data, f, indent=4)

