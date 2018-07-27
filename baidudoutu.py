import re
import requests

params = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': 201326592,
    'is': '',
    'fp': 'result',
    'queryWord': '斗图表情',
    'cl': 2,
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': -1,
    'z': '',
    'ic': '',
    'word': '斗图表情',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '',
    'istype': '',
    'qc': '',
    'nc': 1,
    'fr': '',
    'pn': 30,
    'rn': 30,
    'gsm': '1e',
    '1517455952068': ''
}
pageIndex = 1


def pageRequest(param):
    _index = 1
    html = requests.get('https://image.baidu.com/search/acjson', params=param)
    responseData = html.json()['data']
    for imgData in responseData:
        if 'thumbURL' in imgData:
            pic = requests.get(imgData['thumbURL'])
            fileobj = open('./image/' + str(pageIndex + _index) +
                           str(param['pn']) + '.'+str(imgData['type']), 'wb')
            fileobj.write(pic.content)
            fileobj.close
            _index += 1
            print(imgData['thumbURL'])
for index in range(1, 66):
    print(index)
    params['pn'] = pageIndex * 30
    pageRequest(params)
    pageIndex += 1
