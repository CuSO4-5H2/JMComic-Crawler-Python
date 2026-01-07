from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/1245425/
https://18comic.vip/album/1244775/
https://18comic.vip/album/1244774/
https://18comic.vip/album/1244758/
https://18comic.vip/album/1244756/
https://18comic.vip/album/1244755/
https://18comic.vip/album/1244751/
https://18comic.vip/album/1244745/
https://18comic.vip/album/1244744/
https://18comic.vip/album/1244743/
https://18comic.vip/album/1244739/
https://18comic.vip/album/1244738/
https://18comic.vip/album/1244737/
https://18comic.vip/album/1244735/
https://18comic.vip/album/1244734/
https://18comic.vip/album/1244730/
https://18comic.vip/album/1244717/
https://18comic.vip/album/558369/
https://18comic.vip/album/453036/
https://18comic.vip/album/420734/
https://18comic.vip/album/292633/
https://18comic.vip/album/229037/
https://18comic.vip/album/206346/
https://18comic.vip/album/178633/
https://18comic.vip/album/178154/
https://18comic.vip/album/178153/
https://18comic.vip/album/178152/
https://18comic.vip/album/178121/
https://18comic.vip/album/178120/
https://18comic.vip/album/178119/
https://18comic.vip/album/149976/
https://18comic.vip/album/149849/
https://18comic.vip/album/65141/
https://18comic.vip/album/64615/
https://18comic.vip/album/64300/
https://18comic.vip/album/64218/
https://18comic.vip/album/64175/
https://18comic.vip/album/60450/
https://18comic.vip/album/60446/
https://18comic.vip/album/58023/
https://18comic.vip/album/57769/
https://18comic.vip/album/55604/
https://18comic.vip/album/50249/
https://18comic.vip/album/49843/
https://18comic.vip/album/46937/
https://18comic.vip/album/46935/
https://18comic.vip/album/41557/
https://18comic.vip/album/34433/
https://18comic.vip/album/34056/
https://18comic.vip/album/16009/
https://18comic.vip/album/16000/
https://18comic.vip/album/15982/
https://18comic.vip/album/7362/

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
