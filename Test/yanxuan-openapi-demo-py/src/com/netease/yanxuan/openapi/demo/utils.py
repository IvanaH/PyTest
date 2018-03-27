import datetime
import hashlib
import json


def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def md5(string):
    m = hashlib.md5(string.encode('utf-8'))
    return m.hexdigest()


def get_sign(app_secret, dic):
    param = app_secret
    for key in sorted(dic.keys()):
        value = dic[key]
        if isinstance(value, str):
            param += key + "=" + value
        else:
            param += key + "=" + json.dumps(value)
    param += app_secret
    return md5(param).upper()


def generate_sign(app_secret, string):
    dic = json.loads(string)
    return get_sign(app_secret, dic)


def generate_parameter(app_key, app_secret, method, extra_dic):
    dic = {}
    dic["appKey"] = app_key
    dic["method"] = method
    dic["timestamp"] = get_timestamp()
    if len(extra_dic) > 0:
        dic = dict(dic, **extra_dic)

    dic["sign"] = get_sign(app_secret, dic)

    result = ""
    for key, value in dic.items():
        value_string = value
        if not isinstance(value, str):
            value_string = json.dumps(value)
        result += key + "=" + value_string
        result += "&"
    return result[:-1]
