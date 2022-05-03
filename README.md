# Ob-havo Bot
PyTelegramBotApi - Location)
![Ob-havo](https://user-images.githubusercontent.com/92427513/166525954-31d46fd8-564e-487c-b0f8-1429329a3ff9.png)

## Getting started
This API is tested with Python 3.10 and Pypy 3.
There are two ways to install the library:

* Installation using pip (a Python package manager):

```
$ pip install pyTelegramBotAPI
```
* Installation from source (requires git):

```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install
```
or:
```
$ pip install git+https://github.com/eternnoir/pyTelegramBotAPI.git
```
## Required libraries

geopy is a Python client for several popular geocoding web services.

```
$ pip install geopy
```
## Geocoding
```
$ from geopy.geocoders import Nominatim
$ geolocator = Nominatim(user_agent="specify_your_app_name_here")
$ location = geolocator.geocode("175 5th Avenue NYC")
$ print(location.address)
Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
$ print((location.latitude, location.longitude))
(40.7410861, -73.9896297241625)
$ print(location.raw)
{'place_id': '9167009604', 'type': 'attraction', ...}

```
## Using great-circle distance, also taking pair of (lat, lon) tuples:
```
$ from geopy.distance import great_circle
$ newport_ri = (41.49008, -71.312796)
$ cleveland_oh = (41.499498, -81.695391)
$ print(great_circle(newport_ri, cleveland_oh).miles)
536.997990696
``
