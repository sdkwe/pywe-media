==========
pywe-media
==========

Wechat Media Module for Python.

Sandbox
=======

* https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

Installation
============

::

    pip install pywe-media


Usage
=====

::

    from pywe_media import Media, media_download, media_upload


Method
======

::

    class Media(BaseToken):
        def __init__(self, appid=None, secret=None, token=None, storage=None):
            super(Media, self).__init__(appid=appid, secret=secret, token=token, storage=storage)

    def upload(self, media_type='image', media_file=None, appid=None, secret=None, token=None, storage=None):

    def download(self, media_id, hd=False, appid=None, secret=None, token=None, storage=None):

