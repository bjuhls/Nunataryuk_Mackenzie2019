# by Bennet Juhls (20191010)
# Search and download Sentinel 3 data and save / store metadata in handy formats
# coding: utf-8

from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
MyApi_eumetsat = SentinelAPI( 'username', 'psw', 'https://coda.eumetsat.int/') 

## Learn about keys and values, valid for the **Copernicus data hub**
## by manually selecting search criteria on the web site**
## e.g.:

## TYPE
ProdTyp = "OL_2_WFR___"
ProdNam= "l2_wfr"

## LOCATION
# e.g.:
# location = 'POINT(114.5006 9.9099)'
# or
# footprint = geojson_to_wkt(read_geojson("/map.geojson"))
# or
location = 'POLYGON((-137.57080078125 68.73638345287264, -133.011474609375 68.73638345287264,-133.011474609375 69.54987728327795,-137.57080078125 69.54987728327795,-137.57080078125 68.73638345287264))'

## DATE
# datum = ("29.08.2019", "30.08.2019") in cosy formats e.g. string or python_date_objects
# or
# datum= ('20150802', datetime.datetime.now())
datum = ("20190829", "20190830")

# SEARCH
all_products = MyApi_eumetsat.query(location, date = datum, platformname="Sentinel-3", producttype=ProdTyp, instrumentshortname="OLCI")

## Download

# for product in all_products:
#MyApi.download(product,'/where/to/store/')
 
## GeoJSON FeatureCollection containing footprints and metadata of the scenes
api.to_geojson(all_products)

## GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
api.to_geodataframe(all_products)

## Get basic information about the product: its title, file size, MD5 sum, date, footprint and
## its download url
#api.get_product_odata(<product_id>)

## Get the product's full metadata available on the server
#api.get_product_odata(<product_id>, full=True)


