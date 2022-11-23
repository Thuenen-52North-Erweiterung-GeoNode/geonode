# External Applications

The External Applications app is a contrib module for GeoNode.
The app is compatible with GeoNode v4.

The app adds a model `ExternalApplication` which extends from `GeoApp`.
It integrates as any other resource type so that GeoNode can index, search, and filter an external application like Datasets, Maps, or Dashboards.

## Installation and Configuration

The app must be added to the `INSTALLED_APPS` settings.
Make sure to add it _after_ the `geonode_mapstore_client` app as it makes client configuration adjustments via the mapstore templates.

Create database migrations and apply them via:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Add a Filter Menu

The app adds the resource type `externalapplication` on which you can apply filter on (either by API or mapstore-client search).

If you want the app to create a quick filter menu entry automatically, set `EXTERNAL_APPLICATION_MENU_FILTER_AUTOCREATE=True`.
In case you want to manually add such entry use the GeoNode admin to create a `MenuItem` and point to the URL `/catalogue/#/search/?f=externalapplication`.

