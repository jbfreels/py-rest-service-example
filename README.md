# py-rest-service-example
Using web.py, serve up a simple rest interface.

I created this for another project and decided to table it for now.  I have a requirement to utilize an old version of ArcGIS Server 10.0, current version at time of writing is 10.8.0 beta.  The behemoth of a server application I'm trying to debug has several rest endpoints and some of them take quite a while to return.  I wanted a *simple* and easy to update service I could create multiple endpoints for my UI testing.  

Currently, I'm utilizing a toolbox in ArcGIS Server that mimics the existing calls.  In the future, I'd like to pair this with Selenium and get some automated testing going.  

## setup
The only requirement here is web.py.

`python -m pip install -r requirements.txt`

I've tested this project on
* Windows 10 Pro 64-bit
  * python 3.6.2 64-bit
* Arch Linux (5.3.12)
  * python 3.7.4 64-bit

**should** work with python 2.7, LMK

## running
`python rest-service.py`

Should output something like...

```bash
$ http://0.0.0.0:8080/
```

This signifies the server is running on *localhost* port *8080*.  The port number is configurable in *rest-service.py*, **PORT** var.

## index
I've created the root URL to output the list of running services and the class they call.  If you wanted to utilize `/` for something else, disable/remote *INDEX* object in *json/index.json*

## add new endpoint
* create a response file in *json/* named something helpful (ex. MyNewResponse.json)
* put JSON into your response file
* open *json/index.json*
* add a new item giving it a unique name (ex. MYNEWRESPONSE)
  * *pattern* is the URL without *hostname:port* (ex. "/mynewresponse/GetResponse")
  * *classname* is the class in *core/services.py* the pattern points to (ex. MyNewResponse)
* open *core/services.py*
* create a new class with matching *classname* you just defined (ex. MyNewResponse)
  * *__init\__* pulls in the JSON response file, make sure the filename is correct
  * when a *GET* action is sent to the endpoint, the code in *GET* is executed, we simply return the contents of the JSON response file







If you were looking for ArcGIS Server help I feel bad for ya son.  