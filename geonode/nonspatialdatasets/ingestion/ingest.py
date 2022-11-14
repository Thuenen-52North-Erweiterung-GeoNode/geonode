import psycopg2
import os
import logging

from ..database.database import create_catalog_table, create_dataset_table, insert_data_rows, insert_catalog_entry, query_dataset

logger = logging.getLogger(__name__)

defs = [
    {
        "name": "PointID",
        "type": "integer",
        "description": "Sampling point identifier",
        "primaryKey": True
    },
    {
        "name": "HorizontID",
        "type": "integer",
        "description": "Horizon number of each individual soil profile",
        "primaryKey": True
    },
    {
        "name": "Upper limit",
        "type": "integer",
        "description": "Upper limit of the horizon [cm]"
    }
]

create_catalog_table()
target_table = create_dataset_table("BZE_LW_HORIZON", defs)
print(target_table)
dataset_id = insert_catalog_entry(target_table, defs)
print(dataset_id)

data = [
    [1, 1, 25],
    [1, 2, 50],
    [1, 3, 75],
    [1, 4, 90],
    [1, 5, 95],
    [2, 1, 10],
    [2, 2, 15],
    [2, 3, 16],
    [2, 4, 20],
    [2, 5, 26],
]
insert_data_rows(target_table, defs, data)

data = query_dataset(dataset_id, size=2)
print(data)