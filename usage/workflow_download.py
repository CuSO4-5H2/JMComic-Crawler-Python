from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
https://18comic.vip/album/1224560/
https://18comic.vip/album/1218203/
https://18comic.vip/album/1213709/
https://18comic.vip/album/1209912/
https://18comic.vip/album/1209377/
https://18comic.vip/album/1208026/
https://18comic.vip/album/1205441/
https://18comic.vip/album/1204998/
https://18comic.vip/album/1204536/
https://18comic.vip/album/1200626/
https://18comic.vip/album/1197196/
https://18comic.vip/album/1194285/
https://18comic.vip/album/1194233/
https://18comic.vip/album/1190045/
https://18comic.vip/album/1181711/
https://18comic.vip/album/1173665/
https://18comic.vip/album/1159404/
https://18comic.vip/album/1150169/
https://18comic.vip/album/1149037/
https://18comic.vip/album/1034655/
https://18comic.vip/album/1129720/
https://18comic.vip/album/1125757/
https://18comic.vip/album/1118581/
https://18comic.vip/album/1107435/
https://18comic.vip/album/1093893/
https://18comic.vip/album/1092017/
https://18comic.vip/album/1090124/
https://18comic.vip/album/1090123/
https://18comic.vip/album/1083082/
https://18comic.vip/album/1063028/
https://18comic.vip/album/1028957/
https://18comic.vip/album/1023981/
https://18comic.vip/album/1023930/
https://18comic.vip/album/1023929/
https://18comic.vip/album/1019836/
https://18comic.vip/album/1016793/
https://18comic.vip/album/1015628/
https://18comic.vip/album/651457/
https://18comic.vip/album/651735/
https://18comic.vip/album/642369/
https://18comic.vip/album/637884/
https://18comic.vip/album/636719/
https://18comic.vip/album/614588/
https://18comic.vip/album/609259/
https://18comic.vip/album/605296/
https://18comic.vip/album/602591/
https://18comic.vip/album/584634/
https://18comic.vip/album/579773/
https://18comic.vip/album/576390/
https://18comic.vip/album/574218/
https://18comic.vip/album/573757/
https://18comic.vip/album/564504/
https://18comic.vip/album/561452/
https://18comic.vip/album/557954/
https://18comic.vip/album/553378/
https://18comic.vip/album/546705/
https://18comic.vip/album/545438/
https://18comic.vip/album/539276/
https://18comic.vip/album/374603/
https://18comic.vip/album/535337/
https://18comic.vip/album/535319/
https://18comic.vip/album/534460/
https://18comic.vip/album/533802/
https://18comic.vip/album/533762/
https://18comic.vip/album/526940/
https://18comic.vip/album/511358/
https://18comic.vip/album/503141/
https://18comic.vip/album/502901/
https://18comic.vip/album/500349/
https://18comic.vip/album/485521/
https://18comic.vip/album/471415/
https://18comic.vip/album/469811/
https://18comic.vip/album/469225/
https://18comic.vip/album/461130/
https://18comic.vip/album/458136/
https://18comic.vip/album/452859/
https://18comic.vip/album/441923/
https://18comic.vip/album/439574/
https://18comic.vip/album/438696/
https://18comic.vip/album/438516/
https://18comic.vip/album/433226/
https://18comic.vip/album/432888/
https://18comic.vip/album/432631/
https://18comic.vip/album/430371/
https://18comic.vip/album/425096/
https://18comic.vip/album/425094/
https://18comic.vip/album/417456/
https://18comic.vip/album/407062/
https://18comic.vip/album/406811/
https://18comic.vip/album/405323/
https://18comic.vip/album/401123/
https://18comic.vip/album/398404/
https://18comic.vip/album/393995/
https://18comic.vip/album/391485/
https://18comic.vip/album/389747/
https://18comic.vip/album/387620/
https://18comic.vip/album/380309/
https://18comic.vip/album/379754/
https://18comic.vip/album/374743/
https://18comic.vip/album/374541/
https://18comic.vip/album/374529/
https://18comic.vip/album/369425/
https://18comic.vip/album/365567/
https://18comic.vip/album/361756/
https://18comic.vip/album/360026/
https://18comic.vip/album/356193/
https://18comic.vip/album/356192/
https://18comic.vip/album/356191/
https://18comic.vip/album/355889/
https://18comic.vip/album/350117/
https://18comic.vip/album/347797/
https://18comic.vip/album/346152/
https://18comic.vip/album/346080/
https://18comic.vip/album/341956/
https://18comic.vip/album/340796/
https://18comic.vip/album/335726/
https://18comic.vip/album/334128/
https://18comic.vip/album/333679/
https://18comic.vip/album/331767/
https://18comic.vip/album/330032/
https://18comic.vip/album/330029/
https://18comic.vip/album/329977/
https://18comic.vip/album/326271/
https://18comic.vip/album/323606/
https://18comic.vip/album/321697/
https://18comic.vip/album/321696/
https://18comic.vip/album/320564/
https://18comic.vip/album/319717/
https://18comic.vip/album/318505/
https://18comic.vip/album/315722/
https://18comic.vip/album/314840/
https://18comic.vip/album/314875/
https://18comic.vip/album/314180/
https://18comic.vip/album/310311/
https://18comic.vip/album/309838/
https://18comic.vip/album/308329/
https://18comic.vip/album/307440/
https://18comic.vip/album/305957/
https://18comic.vip/album/305417/
https://18comic.vip/album/305416/
https://18comic.vip/album/305415/
https://18comic.vip/album/305414/
https://18comic.vip/album/305413/
https://18comic.vip/album/305412/
https://18comic.vip/album/305403/
https://18comic.vip/album/304765/
https://18comic.vip/album/304759/
https://18comic.vip/album/300726/
https://18comic.vip/album/299068/
https://18comic.vip/album/297237/
https://18comic.vip/album/295978/
https://18comic.vip/album/294555/
https://18comic.vip/album/293255/
https://18comic.vip/album/292306/
https://18comic.vip/album/292258/
https://18comic.vip/album/290540/
https://18comic.vip/album/290016/
https://18comic.vip/album/289726/
https://18comic.vip/album/274125/
https://18comic.vip/album/276028/
https://18comic.vip/album/262419/
https://18comic.vip/album/258587/
https://18comic.vip/album/258586/
https://18comic.vip/album/253780/
https://18comic.vip/album/251848/
https://18comic.vip/album/251847/
https://18comic.vip/album/234480/
https://18comic.vip/album/232149/
https://18comic.vip/album/232057/
https://18comic.vip/album/190054/
https://18comic.vip/album/147751/
https://18comic.vip/album/189223/
https://18comic.vip/album/122547/
https://18comic.vip/album/93632/
https://18comic.vip/album/93145/
https://18comic.vip/album/82787/
https://18comic.vip/album/51336/
https://18comic.vip/album/51113/
https://18comic.vip/album/48671/
https://18comic.vip/album/43069/
https://18comic.vip/album/37345/
https://18comic.vip/album/30215/
https://18comic.vip/album/23633/
https://18comic.vip/album/10771/
https://18comic.vip/album/9214/
https://18comic.vip/album/7724/
https://18comic.vip/album/5574/
https://18comic.vip/album/1530/
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
