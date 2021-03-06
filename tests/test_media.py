# -*- coding: utf-8 -*-

import requests
from pywe_media import Media, media_download, media_downloadurl, media_upload, media_uploadimg

from local_wecfg_example import IMAGE_PATH, WECHAT


class TestMediaCommands(object):

    def test_media(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        media_file = open(IMAGE_PATH, 'rb')
        media = Media(appid=appid, secret=appsecret)
        data = media.upload(media_file=media_file)
        # {u'media_id': u'KptzZFv35-iSWE6cgmsQpaeqw986IjcFlqumgm_IEkP3-8-wyMDJNw12H4b4RPVP', u'created_at': 1503983273, u'type': u'image'}
        assert isinstance(data, dict)
        assert data.get('media_id', '')

        media_id = data.get('media_id', '')
        data = media.download(media_id, appid=appid, secret=appsecret)
        assert isinstance(data, requests.Response)
        assert data.status_code == 200

    def test_media_upload_download(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        # media_file = open(IMAGE_PATH, 'rb')
        data = media_upload(media_file=None, media_file_path=IMAGE_PATH, appid=appid, secret=appsecret)
        # {u'media_id': u'KptzZFv35-iSWE6cgmsQpaeqw986IjcFlqumgm_IEkP3-8-wyMDJNw12H4b4RPVP', u'created_at': 1503983273, u'type': u'image'}
        assert isinstance(data, dict)
        assert data.get('media_id', '')

        media_id = data.get('media_id', '')
        data = media_download(media_id, appid=appid, secret=appsecret)
        assert isinstance(data, requests.Response)
        assert data.status_code == 200

    def test_invalid_mediaid_error(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        data = media_download('invalid_mediaid', appid=appid, secret=appsecret)
        assert isinstance(data, requests.Response)
        assert data.status_code == 200
        # {"errcode": 40007, "errmsg": "invalid media_id hint: [CNRD70014e298]"}
        assert data.json()['errcode'] == 40007

    def test_invalid_accesstoken_error(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        data = media_download('media_id', appid=appid, secret=appsecret, token='invalid_accesstoken')
        assert isinstance(data, requests.Response)
        assert data.status_code == 200
        # {"errcode": 40001, "errmsg": "invalid credential, access_token is invalid or not latest hint: [9kOn80882vr45!]"}
        assert data.json()['errcode'] == 40001

    def test_downloadurl(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        downloadurl = media_downloadurl('media_id', appid=appid, secret=appsecret, token='invalid_accesstoken')
        assert isinstance(downloadurl, basestring)

    def test_media_uploadimg(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        media_file = open(IMAGE_PATH, 'rb')
        media = Media(appid=appid, secret=appsecret)
        data = media.uploadimg(media_file=media_file)
        # {"url":  "http://mmbiz.qpic.cn/mmbiz/gLO17UPS6FS2xsypf378iaNhWacZ1G1UplZYWEYfwvuU6Ont96b1roYs CNFwaRrSaKTPCUdBK9DgEHicsKwWCBRQ/0"}
        assert isinstance(data, dict)
        assert data.get('url', '')

        data2 = media_uploadimg(media_file_path=IMAGE_PATH, appid=appid, secret=appsecret, forcard=True)
        assert isinstance(data2, dict)
        assert data2.get('url', '')

        assert data.get('url', '') == data2.get('url', '')
