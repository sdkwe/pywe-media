# -*- coding: utf-8 -*-

from pywe_token import BaseToken, final_access_token


class Media(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(Media, self).__init__(appid=appid, secret=secret, token=token, storage=storage)
        # 新增临时素材, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738726
        self.WECHAT_MEDIA_UPLOAD = self.API_DOMAIN + '/cgi-bin/media/upload'
        # 获取临时素材, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738727
        self.WECHAT_MEDIA_GET = self.API_DOMAIN + '/cgi-bin/media/get?access_token={access_token}&media_id={media_id}'
        # 高清语音素材获取接口, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738727
        self.WECHAT_MEDIA_GET_JSSDK = self.API_DOMAIN + '/cgi-bin/media/get/jssdk?access_token={access_token}&media_id={media_id}'
        # 新增永久素材, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738729
        # 上传图文消息内的图片获取URL
        # 创建卡券, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1451025056
        # 2.3 步骤一：上传卡券图片素材
        self.WECHAT_MEDIA_UPLOADIMG = self.API_DOMAIN + '/cgi-bin/media/uploadimg'

    def upload(self, media_type='image', media_file=None, media_file_path=None, appid=None, secret=None, token=None, storage=None):
        """
        :param media_type: 媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb）
        :param media_file: 要上传的文件，一个 File-object
        """
        return self.post(
            self.WECHAT_MEDIA_UPLOAD,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
                'type': media_type,
            },
            files={
                'media': media_file or open(media_file_path, 'rb'),
            },
        )

    def download(self, media_id, hd=False, appid=None, secret=None, token=None, storage=None):
        return self.get(self.WECHAT_MEDIA_GET_JSSDK if hd else self.WECHAT_MEDIA_GET, access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage), media_id=media_id, res_to_json=False)

    def downloadurl(self, media_id, hd=False, appid=None, secret=None, token=None, storage=None):
        return self.geturl(self.WECHAT_MEDIA_GET_JSSDK if hd else self.WECHAT_MEDIA_GET, access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage), media_id=media_id)

    def uploadimg(self, media_file=None, media_file_path=None, appid=None, secret=None, token=None, storage=None, forcard=False):
        media_file = media_file or open(media_file_path, 'rb')
        files = {
            'buffer': media_file,
        } if forcard else {
            'media': media_file,
        }
        return self.post(
            self.WECHAT_MEDIA_UPLOADIMG,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            files=files,
        )


media = Media()
media_upload = media.upload
media_download = media.download
media_downloadurl = media.downloadurl
media_uploadimg = media.uploadimg
