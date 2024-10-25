from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/393756
https://18comic.vip/album/517022
https://18comic.vip/album/347417
https://18comic.vip/album/292121
https://18comic.vip/album/292250
https://18comic.vip/album/575911
https://18comic.vip/album/401192
https://18comic.vip/album/347463
https://18comic.vip/album/291226
https://18comic.vip/album/225612
https://18comic.vip/album/150887
https://18comic.vip/album/116107
https://18comic.vip/album/99950
https://18comic.vip/album/99949
https://18comic.vip/album/99948
https://18comic.vip/album/99947
https://18comic.vip/album/99946
https://18comic.vip/album/99944
https://18comic.vip/album/99945
https://18comic.vip/album/99943
https://18comic.vip/album/99942
https://18comic.vip/album/99941
https://18comic.vip/album/99940
https://18comic.vip/album/99939
https://18comic.vip/album/99938
https://18comic.vip/album/95685
https://18comic.vip/album/95660
https://18comic.vip/album/79453
https://18comic.vip/album/79378
https://18comic.vip/album/79377
https://18comic.vip/album/79376
https://18comic.vip/album/79374
https://18comic.vip/album/79373
https://18comic.vip/album/78463
https://18comic.vip/album/78462
https://18comic.vip/album/78460
https://18comic.vip/album/78461
https://18comic.vip/album/78459
https://18comic.vip/album/78346
https://18comic.vip/album/78345
https://18comic.vip/album/78259
https://18comic.vip/album/78258
https://18comic.vip/album/78126
https://18comic.vip/album/78117
https://18comic.vip/album/78116
https://18comic.vip/album/73747
https://18comic.vip/album/36269
https://18comic.vip/album/36256
https://18comic.vip/album/20045
https://18comic.vip/album/20039
https://18comic.vip/album/20038
https://18comic.vip/album/19995
https://18comic.vip/album/9522
https://18comic.vip/album/9277
https://18comic.vip/album/5971
https://18comic.vip/album/5967
https://18comic.vip/album/521257
https://18comic.vip/album/496420
https://18comic.vip/album/442131
https://18comic.vip/album/347691
https://18comic.vip/album/335759
https://18comic.vip/album/235559
https://18comic.vip/album/205679
https://18comic.vip/album/148723
https://18comic.vip/album/122294
https://18comic.vip/album/121942
https://18comic.vip/album/113137
https://18comic.vip/album/107219
https://18comic.vip/album/107220
https://18comic.vip/album/105975
https://18comic.vip/album/105971
https://18comic.vip/album/105336
https://18comic.vip/album/100636
https://18comic.vip/album/100635
https://18comic.vip/album/100634
https://18comic.vip/album/100633
https://18comic.vip/album/99869
https://18comic.vip/album/94227
https://18comic.vip/album/85399
https://18comic.vip/album/84935
https://18comic.vip/album/80645
https://18comic.vip/album/75865
https://18comic.vip/album/75811
https://18comic.vip/album/70687
https://18comic.vip/album/70595
https://18comic.vip/album/53926
https://18comic.vip/album/53845
https://18comic.vip/album/51330
https://18comic.vip/album/51328
https://18comic.vip/album/51326
https://18comic.vip/album/42722
https://18comic.vip/album/40410
https://18comic.vip/album/39273
https://18comic.vip/album/36233
https://18comic.vip/album/33784
https://18comic.vip/album/33192
https://18comic.vip/album/30012
https://18comic.vip/album/29821
https://18comic.vip/album/25612
https://18comic.vip/album/23521
https://18comic.vip/album/22118
https://18comic.vip/album/22119
https://18comic.vip/album/22115
https://18comic.vip/album/22113
https://18comic.vip/album/22112
https://18comic.vip/album/22109
https://18comic.vip/album/22108
https://18comic.vip/album/22107
https://18comic.vip/album/22106
https://18comic.vip/album/22104
https://18comic.vip/album/22103
https://18comic.vip/album/22100
https://18comic.vip/album/22098
https://18comic.vip/album/22097
https://18comic.vip/album/22095
https://18comic.vip/album/22094
https://18comic.vip/album/22093
https://18comic.vip/album/21802
https://18comic.vip/album/20927
https://18comic.vip/album/20213
https://18comic.vip/album/10764
https://18comic.vip/album/8377
https://18comic.vip/album/5779
https://18comic.vip/album/2200
'''

# 单独下载章节
jm_photos = '''



'''


def env(name, default, trim=('[]', '""', "''")):
    import os
    value = os.getenv(name, None)
    if value is None or value == '':
        return default

    for pair in trim:
        if value.startswith(pair[0]) and value.endswith(pair[1]):
            value = value[1:-1]

    return value


def get_id_set(env_name, given):
    aid_set = set()
    for text in [
        given,
        (env(env_name, '')).replace('-', '\n'),
    ]:
        aid_set.update(str_to_set(text))

    return aid_set


def main():
    album_id_set = get_id_set('JM_ALBUM_IDS', jm_albums)
    photo_id_set = get_id_set('JM_PHOTO_IDS', jm_photos)

    helper = JmcomicUI()
    helper.album_id_list = list(album_id_set)
    helper.photo_id_list = list(photo_id_set)

    option = get_option()
    helper.run(option)
    option.call_all_plugin('after_download')


def get_option():
    # 读取 option 配置文件
    option = create_option(os.path.abspath(os.path.join(__file__, '../../assets/option/option_workflow_download.yml')))

    # 支持工作流覆盖配置文件的配置
    cover_option_config(option)

    # 把请求错误的html下载到文件，方便GitHub Actions下载查看日志
    log_before_raise()

    return option


def cover_option_config(option: JmOption):
    dir_rule = env('DIR_RULE', None)
    if dir_rule is not None:
        the_old = option.dir_rule
        the_new = DirRule(dir_rule, base_dir=the_old.base_dir)
        option.dir_rule = the_new

    impl = env('CLIENT_IMPL', None)
    if impl is not None:
        option.client.impl = impl

    suffix = env('IMAGE_SUFFIX', None)
    if suffix is not None:
        option.download.image.suffix = fix_suffix(suffix)


def log_before_raise():
    jm_download_dir = env('JM_DOWNLOAD_DIR', workspace())
    mkdir_if_not_exists(jm_download_dir)

    def decide_filepath(e):
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)

        if resp is None:
            suffix = str(time_stamp())
        else:
            suffix = resp.url

        name = '-'.join(
            fix_windir_name(it)
            for it in [
                e.description,
                current_thread().name,
                suffix
            ]
        )

        path = f'{jm_download_dir}/【出错了】{name}.log'
        return path

    def exception_listener(e: JmcomicException):
        """
        异常监听器，实现了在 GitHub Actions 下，把请求错误的信息下载到文件，方便调试和通知使用者
        """
        # 决定要写入的文件路径
        path = decide_filepath(e)

        # 准备内容
        content = [
            str(type(e)),
            e.msg,
        ]
        for k, v in e.context.items():
            content.append(f'{k}: {v}')

        # resp.text
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)
        if resp:
            content.append(f'响应文本: {resp.text}')

        # 写文件
        write_text(path, '\n'.join(content))

    JmModuleConfig.register_exception_listener(JmcomicException, exception_listener)


if __name__ == '__main__':
    main()
