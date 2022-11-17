from django.db import models
from geonode.base.models import ResourceBase

class NonSpatialDataset(ResourceBase):
    
    postgres_url = models.URLField(
        'Postgres URL',
        null=True,
        blank=True,
        help_text='The Postgres connection string as a URL (optional). If empty, the API will lookup the default GeoNode database')
    
    database_table = models.CharField('Database Table', max_length=255, null=True, blank=True)
    
    column_definitions = models.TextField('Column Definitions')

    def get_absolute_url(self):
        return f"/nonspatial/{self.pk}"
