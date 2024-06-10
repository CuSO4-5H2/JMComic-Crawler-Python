from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/580667
https://18comic.vip/album/574780
https://18comic.vip/album/574779
https://18comic.vip/album/574777
https://18comic.vip/album/562102
https://18comic.vip/album/553577
https://18comic.vip/album/551298
https://18comic.vip/album/487798
https://18comic.vip/album/508373
https://18comic.vip/album/508372
https://18comic.vip/album/508370
https://18comic.vip/album/508363
https://18comic.vip/album/508359
https://18comic.vip/album/508356
https://18comic.vip/album/508354
https://18comic.vip/album/481849
https://18comic.vip/album/481847
https://18comic.vip/album/481845
https://18comic.vip/album/477346
https://18comic.vip/album/431059
https://18comic.vip/album/429938
https://18comic.vip/album/424899
https://18comic.vip/album/419423
https://18comic.vip/album/396079
https://18comic.vip/album/392485
https://18comic.vip/album/386737
https://18comic.vip/album/383640
https://18comic.vip/album/376390
https://18comic.vip/album/361068
https://18comic.vip/album/361067
https://18comic.vip/album/353595
https://18comic.vip/album/335479
https://18comic.vip/album/333249
https://18comic.vip/album/324542
https://18comic.vip/album/324540
https://18comic.vip/album/324539
https://18comic.vip/album/324536
https://18comic.vip/album/314216
https://18comic.vip/album/304058
https://18comic.vip/album/297952
https://18comic.vip/album/295663
https://18comic.vip/album/292209
https://18comic.vip/album/282681
https://18comic.vip/album/277859
https://18comic.vip/album/270946
https://18comic.vip/album/264531
https://18comic.vip/album/262426
https://18comic.vip/album/260124
https://18comic.vip/album/255862
https://18comic.vip/album/254760
https://18comic.vip/album/252576
https://18comic.vip/album/250340
https://18comic.vip/album/249188
https://18comic.vip/album/244962
https://18comic.vip/album/243936
https://18comic.vip/album/239290
https://18comic.vip/album/233731
https://18comic.vip/album/231354
https://18comic.vip/album/230927
https://18comic.vip/album/228415
https://18comic.vip/album/227513
https://18comic.vip/album/226342
https://18comic.vip/album/226155
https://18comic.vip/album/225903
https://18comic.vip/album/223377
https://18comic.vip/album/222558
https://18comic.vip/album/222440
https://18comic.vip/album/217598
https://18comic.vip/album/213884
https://18comic.vip/album/213778
https://18comic.vip/album/209225
https://18comic.vip/album/205822
https://18comic.vip/album/203961
https://18comic.vip/album/197417
https://18comic.vip/album/189217
https://18comic.vip/album/188604
https://18comic.vip/album/181346
https://18comic.vip/album/180054
https://18comic.vip/album/179584
https://18comic.vip/album/179581
https://18comic.vip/album/178178
https://18comic.vip/album/151372
https://18comic.vip/album/165848
https://18comic.vip/album/140709
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
