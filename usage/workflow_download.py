from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/1025767
https://18comic.vip/album/1025766
https://18comic.vip/album/1025765
https://18comic.vip/album/1025494
https://18comic.vip/album/1025493
https://18comic.vip/album/1025492
https://18comic.vip/album/1025491
https://18comic.vip/album/1024375
https://18comic.vip/album/1021299
https://18comic.vip/album/1020009
https://18comic.vip/album/652168
https://18comic.vip/album/651166
https://18comic.vip/album/647955
https://18comic.vip/album/646838
https://18comic.vip/album/646835
https://18comic.vip/album/643956
https://18comic.vip/album/642944
https://18comic.vip/album/638687
https://18comic.vip/album/637383
https://18comic.vip/album/635483
https://18comic.vip/album/632802
https://18comic.vip/album/628532
https://18comic.vip/album/625250
https://18comic.vip/album/614643
https://18comic.vip/album/568642
https://18comic.vip/album/568640
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
https://18comic.vip/album/542849
https://18comic.vip/album/542848
https://18comic.vip/album/542847
https://18comic.vip/album/542846
https://18comic.vip/album/542835
https://18comic.vip/album/542834
https://18comic.vip/album/542669
https://18comic.vip/album/541806
https://18comic.vip/album/540892
https://18comic.vip/album/539914
https://18comic.vip/album/516982
https://18comic.vip/album/505014
https://18comic.vip/album/498251
https://18comic.vip/album/485969
https://18comic.vip/album/469798
https://18comic.vip/album/438505
https://18comic.vip/album/433941
https://18comic.vip/album/390359
https://18comic.vip/album/389219
https://18comic.vip/album/388725
https://18comic.vip/album/385485
https://18comic.vip/album/384049
https://18comic.vip/album/383686
https://18comic.vip/album/369778
https://18comic.vip/album/293845
https://18comic.vip/album/290791
https://18comic.vip/album/290790
https://18comic.vip/album/290788
https://18comic.vip/album/290787
https://18comic.vip/album/290786
https://18comic.vip/album/290785
https://18comic.vip/album/290594
https://18comic.vip/album/282732
https://18comic.vip/album/274665
https://18comic.vip/album/267752
https://18comic.vip/album/1023746
https://18comic.vip/album/1022517
https://18comic.vip/album/1022450
https://18comic.vip/album/1022014
https://18comic.vip/album/598514
https://18comic.vip/album/563917
https://18comic.vip/album/507776
https://18comic.vip/album/440725
https://18comic.vip/album/422855
https://18comic.vip/album/414830
https://18comic.vip/album/384503
https://18comic.vip/album/383450
https://18comic.vip/album/355632
https://18comic.vip/album/337577
https://18comic.vip/album/314913
https://18comic.vip/album/293619
https://18comic.vip/album/282746
https://18comic.vip/album/281324
https://18comic.vip/album/280684
https://18comic.vip/album/277013
https://18comic.vip/album/269614
https://18comic.vip/album/257778
https://18comic.vip/album/250045
https://18comic.vip/album/226834
https://18comic.vip/album/221653
https://18comic.vip/album/221652
https://18comic.vip/album/189718
https://18comic.vip/album/189717
https://18comic.vip/album/189716
https://18comic.vip/album/149705
https://18comic.vip/album/142609
https://18comic.vip/album/138343
https://18comic.vip/album/1024988
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
