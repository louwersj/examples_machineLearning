__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load a simple .json file into a DataFrame based upon a remote .json file. the JSON 
    comes from a ORDS endpoint and provides a JSON representation of the query "SELECT deptno FROM emp" which is 
    standard oracle demo table. The JSON structure contains more than only the data we require, we require only the
    data which resides under items. By default ORDS JSON structures also contain elements like hasMore, limit, offset, 
    count and links. In our case we do not want to capture this information within our DataFrame, we are only interested 
    in the item elements. 

    this example is basically the same as pd_read_example_3.py with the difference that we load the JSON from local
    disk instead of retrieving it from a remote endpoint using a http connections. 
'''

import json
from urllib2 import urlopen
from pandas.io.json import json_normalize

# Fetch the data from the remote ORDS endpoint
#apiResponse = urlopen("http://192.168.33.10:8080/ords/pandas_test/test/employees")
#apiResponseFile = apiResponse.read().decode('utf-8', 'replace')

# load the JSON data we fetched from the ORDS endpoint into a dict
#jsonData = json.loads('../../data/dataset_7.json')

# load the dict containing the JSON data into a DataFrame by using json_normalized, do note we only use 'items'
#df = json_normalize(jsonData['items'])
df0 = json_normalize('../../data/dataset_6.json'['items'])

# show the evidence we received the data from the ORDS endpoint.
print (df0.head())

