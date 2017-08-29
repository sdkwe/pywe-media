# -*- coding: utf-8 -*-

from pywe_base import BaseWechat
from pywe_storage import MemoryStorage
from pywe_token import access_token


class Media(BaseWechat):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(Media, self).__init__()
        # 新增临时素材, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738726
        self.WECHAT_MEDIA_UPLOAD = self.API_DOMAIN + '/cgi-bin/media/upload'
        # 获取临时素材, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738727
        self.WECHAT_MEDIA_GET = self.API_DOMAIN + '/cgi-bin/media/get?access_token={access_token}&media_id={media_id}'
        self.appid = appid
        self.secret = secret
        self.token = token
        self.storage = storage or MemoryStorage()

    def upload(self, media_type='image', media_file=None, appid=None, secret=None, token=None, storage=None):
        """
        :param media_type: 媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb）
        :param media_file: 要上传的文件，一个 File-object
        """
        return self.post(
            self.WECHAT_MEDIA_UPLOAD,
            params={
                'access_token': token or self.token or access_token(appid or self.appid, secret or self.secret, storage=storage or self.storage),
                'type': media_type
            },
            files={
                'media': media_file
            }
        )

    def download(self, media_id, appid=None, secret=None, token=None, storage=None):
        return self.get(self.WECHAT_MEDIA_GET, access_token=token or self.token or access_token(appid or self.appid, secret or self.secret, storage=storage or self.storage), media_id=media_id, tojson=False)


media = Media()
media_upload = media.upload
media_download = media.download
