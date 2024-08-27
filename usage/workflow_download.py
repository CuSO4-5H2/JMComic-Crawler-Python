from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/614643
https://18comic.vip/album/602613
https://18comic.vip/album/564510
https://18comic.vip/album/562167
https://18comic.vip/album/562163
https://18comic.vip/album/562159
https://18comic.vip/album/562158
https://18comic.vip/album/562157
https://18comic.vip/album/562156
https://18comic.vip/album/562155
https://18comic.vip/album/562154
https://18comic.vip/album/562153
https://18comic.vip/album/562152
https://18comic.vip/album/562150
https://18comic.vip/album/562147
https://18comic.vip/album/562129
https://18comic.vip/album/562128
https://18comic.vip/album/505014
https://18comic.vip/album/498251
https://18comic.vip/album/433941
https://18comic.vip/album/393997
https://18comic.vip/album/393996
https://18comic.vip/album/389219
https://18comic.vip/album/284501
https://18comic.vip/album/215548
https://18comic.vip/album/194493
https://18comic.vip/album/602074
https://18comic.vip/album/567329
https://18comic.vip/album/561012
https://18comic.vip/album/541161
https://18comic.vip/album/515237
https://18comic.vip/album/512809
https://18comic.vip/album/505730
https://18comic.vip/album/502898
https://18comic.vip/album/495907
https://18comic.vip/album/482306
https://18comic.vip/album/473964
https://18comic.vip/album/450065
https://18comic.vip/album/392773
https://18comic.vip/album/408259
https://18comic.vip/album/392674
https://18comic.vip/album/392662
https://18comic.vip/album/392640
https://18comic.vip/album/377487
https://18comic.vip/album/330967
https://18comic.vip/album/301649
https://18comic.vip/album/275932
https://18comic.vip/album/275929
https://18comic.vip/album/275927
https://18comic.vip/album/228026
https://18comic.vip/album/177636
https://18comic.vip/album/144628
https://18comic.vip/album/144574
https://18comic.vip/album/140296
https://18comic.vip/album/123382
https://18comic.vip/album/121759
https://18comic.vip/album/114803
https://18comic.vip/album/515070
https://18comic.vip/album/512896
https://18comic.vip/album/511556
https://18comic.vip/album/511555
https://18comic.vip/album/511369
https://18comic.vip/album/129733
https://18comic.vip/album/511368
https://18comic.vip/album/511367
https://18comic.vip/album/378246
https://18comic.vip/album/377413
https://18comic.vip/album/333728
https://18comic.vip/album/315961
https://18comic.vip/album/213004
https://18comic.vip/album/239770
https://18comic.vip/album/226246
https://18comic.vip/album/226243
https://18comic.vip/album/226242
https://18comic.vip/album/226240
https://18comic.vip/album/226239
https://18comic.vip/album/226238
https://18comic.vip/album/223838
https://18comic.vip/album/215769
https://18comic.vip/album/220907
https://18comic.vip/album/215521
https://18comic.vip/album/215580
https://18comic.vip/album/149360
https://18comic.vip/album/144707
https://18comic.vip/album/603144
https://18comic.vip/album/582135
https://18comic.vip/album/603976
https://18comic.vip/album/602614
https://18comic.vip/album/602125
https://18comic.vip/album/600128
https://18comic.vip/album/478179
https://18comic.vip/album/469238
https://18comic.vip/album/465561
https://18comic.vip/album/355950
https://18comic.vip/album/455090
https://18comic.vip/album/453118
https://18comic.vip/album/442899
https://18comic.vip/album/410609
https://18comic.vip/album/380458
https://18comic.vip/album/379760
https://18comic.vip/album/370636
https://18comic.vip/album/335433
https://18comic.vip/album/307582
https://18comic.vip/album/601321
https://18comic.vip/album/601320
https://18comic.vip/album/601319
https://18comic.vip/album/601318
https://18comic.vip/album/601317
https://18comic.vip/album/601316
https://18comic.vip/album/601315
https://18comic.vip/album/601314
https://18comic.vip/album/601313
https://18comic.vip/album/601312
https://18comic.vip/album/601311
https://18comic.vip/album/601310
https://18comic.vip/album/601309
https://18comic.vip/album/601308
https://18comic.vip/album/601307
https://18comic.vip/album/601306
https://18comic.vip/album/601305
https://18comic.vip/album/601303
https://18comic.vip/album/601302
https://18comic.vip/album/601301
https://18comic.vip/album/601300
https://18comic.vip/album/601299
https://18comic.vip/album/601298
https://18comic.vip/album/601297
https://18comic.vip/album/601296
https://18comic.vip/album/601295
https://18comic.vip/album/601294
https://18comic.vip/album/601293
https://18comic.vip/album/601292
https://18comic.vip/album/601291
https://18comic.vip/album/601290
https://18comic.vip/album/598491
https://18comic.vip/album/571927
https://18comic.vip/album/562423
https://18comic.vip/album/552843
https://18comic.vip/album/515898
https://18comic.vip/album/508809
https://18comic.vip/album/406360
https://18comic.vip/album/401588
https://18comic.vip/album/400940
https://18comic.vip/album/394151
https://18comic.vip/album/343183
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
