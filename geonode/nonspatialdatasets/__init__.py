import logging
from .database.database import create_catalog_table

logger = logging.getLogger(__name__)

# general setup of meta/catalog table
create_catalog_table()