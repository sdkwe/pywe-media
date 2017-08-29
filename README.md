# pywe-media

Wechat Media Module for Python.

# Installation

```shell
pip install pywe-media
```

# Usage

```python
from pywe_media import Media, media_download, media_upload
```

# Method

```python
class Media(BaseWechat):
    def __init__(self, appid=None, secret=None, token=None, storage=None):

def upload(self, media_type='image', media_file=None, appid=None, secret=None, token=None, storage=None):

def download(self, media_id, appid=None, secret=None, token=None, storage=None):

def jsapi_ticket(self, appid=None, secret=None, token=None, storage=None):

def refresh_ticket(self, appid=None, secret=None, token=None, type='jsapi', storage=None):
```
