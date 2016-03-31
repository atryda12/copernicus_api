# copernicus_api
API for Copernicus for IoT classes on AGh UST Faculty of Computer Science, Electronics and Telecommunications
The description of a tool can be found [here](http://galaxy.agh.edu.pl/~tszydlo/copernicus/).
This API is compiliant with tables of requests and responses in the above link.

## 'long' version
Stndard API is contained in copernicus_api.py file. I believe names are quite self explanatory

While using 
```python
copernicus_api.Request.for_automatic_updates_of(*args)
copernicus_api.Request.query_for_parmaeters_of(*args)
```
`*args` is a vararg list of desired `copernicus_api.QueryableComponent`.

Class `Response` is not yet safe - you may get illegal value of parameter from response if you use QyeryableComponent wich response does not contain.

Argument for  `copernicus_api.Rerquest.to_set_rgb_of_led2(rgb)` is an object of class `copernicus_api.Rgb3`

## 'short' version
Short version contains aliases to be used while not working in ide and under pressure of time (like during class, coding on the device throu vi by ssh)

recommended import for this is
```python
from ca_short import *
```

Besides shorter names of helper methods instead of class methods there are 2 differences:
* `set_led2` takes three values of r, g, and b instead of `Rgb3` object
* Copernicus object is created on the fly while requesting and getting response.
