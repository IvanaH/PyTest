import requests
import utils

appKey = ""
appSecret = ""


def main():
    print('start')
    print(get_ids())


def get_ids():
    dic = {"itemIds": "1085002"}
    method = "yanxuan.item.batch.get"
    url = 'http://openapi-test.you.163.com/channel/api.json'
    r = requests.post(url, params=utils.generate_parameter(appKey, appSecret, method, dic))
    return r.text


main()
