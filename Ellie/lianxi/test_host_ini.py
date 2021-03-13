import configparser
import os


def test_get_config():
    config = configparser.ConfigParser()
    # os.environ['HOME']
    # xpath = os.path.join(os.environ['HOMEPATH'], 'host.ini')
    xpath = 'D:/拉钩/work/pythonProject/Ellie/lianxi/host.ini'
    config.read(xpath)
    r = config.options("mysql")
    print(r)
    print(config.get('mysql','host'))
    print(config.items("mysql"))
    return config

    # print('获取配置文件所有的section', sections)
    #
    # options = conf.options('mysql')
    # print('获取指定section下所有option', options)
    #
    # items = conf.items('mysql')
    # print('获取指定section下所有的键值对', items)
    #
    # value = conf.get('mysql', 'host')
    # print('获取指定的section下的option', type(value), value)
