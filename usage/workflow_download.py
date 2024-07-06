from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/589561
https://18comic.vip/album/575499
https://18comic.vip/album/563498
https://18comic.vip/album/469222
https://18comic.vip/album/485711
https://18comic.vip/album/503487
https://18comic.vip/album/495060
https://18comic.vip/album/584042
https://18comic.vip/album/579625
https://18comic.vip/album/578564
https://18comic.vip/album/578546
https://18comic.vip/album/589363
https://18comic.vip/album/588438
https://18comic.vip/album/568329
https://18comic.vip/album/500520
https://18comic.vip/album/587873
https://18comic.vip/album/587872
https://18comic.vip/album/587871
https://18comic.vip/album/587870
https://18comic.vip/album/587869
https://18comic.vip/album/587868
https://18comic.vip/album/576347
https://18comic.vip/album/571061
https://18comic.vip/album/571060
https://18comic.vip/album/571059
https://18comic.vip/album/571058
https://18comic.vip/album/571057
https://18comic.vip/album/571056
https://18comic.vip/album/571055
https://18comic.vip/album/571054
https://18comic.vip/album/571053
https://18comic.vip/album/571052
https://18comic.vip/album/571051
https://18comic.vip/album/571050
https://18comic.vip/album/571049
https://18comic.vip/album/571048
https://18comic.vip/album/576806
https://18comic.vip/album/576805
https://18comic.vip/album/576342
https://18comic.vip/album/576341
https://18comic.vip/album/576335
https://18comic.vip/album/576334
https://18comic.vip/album/576331
https://18comic.vip/album/575914
https://18comic.vip/album/575792
https://18comic.vip/album/575791
https://18comic.vip/album/575337
https://18comic.vip/album/575336
https://18comic.vip/album/575335
https://18comic.vip/album/575334
https://18comic.vip/album/575330
https://18comic.vip/album/517727
https://18comic.vip/album/503101
https://18comic.vip/album/502435
https://18comic.vip/album/496416
https://18comic.vip/album/458436
https://18comic.vip/album/450853
https://18comic.vip/album/450850
https://18comic.vip/album/397754
https://18comic.vip/album/433276
https://18comic.vip/album/334745
https://18comic.vip/album/404380
https://18comic.vip/album/400314
https://18comic.vip/album/280948
https://18comic.vip/album/250433
https://18comic.vip/album/397749
https://18comic.vip/album/389767
https://18comic.vip/album/369589
https://18comic.vip/album/324502
https://18comic.vip/album/273265
https://18comic.vip/album/269638
https://18comic.vip/album/257391
https://18comic.vip/album/580638
https://18comic.vip/album/553373
https://18comic.vip/album/547476
https://18comic.vip/album/547475
https://18comic.vip/album/547460
https://18comic.vip/album/547459
https://18comic.vip/album/497688
https://18comic.vip/album/497192
https://18comic.vip/album/496923
https://18comic.vip/album/496880
https://18comic.vip/album/496879
https://18comic.vip/album/487068
https://18comic.vip/album/487067
https://18comic.vip/album/466386
https://18comic.vip/album/407511
https://18comic.vip/album/357623
https://18comic.vip/album/407428
https://18comic.vip/album/376630
https://18comic.vip/album/585350
https://18comic.vip/album/585329
https://18comic.vip/album/491311
https://18comic.vip/album/413867
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
