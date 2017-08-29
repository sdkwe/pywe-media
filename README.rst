==========
pywe-media
==========

Wechat Media Module for Python.

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

    class Media(BaseWechat):
        def __init__(self, appid=None, secret=None, token=None, storage=None):

    def upload(self, media_type='image', media_file=None, appid=None, secret=None, token=None, storage=None):

    def download(self, media_id, appid=None, secret=None, token=None, storage=None):

