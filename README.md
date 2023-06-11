# django-imagekit-uploadfile
A small project, that will upload media files in imagekit server.

### Install Dependecies
```console
pip install imagekitio
```
```console
pip install django
```
```console
pip install python-dotenv
```

### Create ```.env``` file, where ```manage.py``` is located

```
IMAGEKIT_PUBLIC_KEY="add here imagekit public key"
IMAGEKIT_PRIVATE_KEY="add here imagekit private key"
IMAGEKIT_URL_ENDPOINT="add here imagekit url endpoint"
```
### Get imagekit credentials
To get a imagekit credentials, just create an account in <a href="imagekit.io">imagekit</a>. In Developer option, you can get here public, private and url endpoint.
