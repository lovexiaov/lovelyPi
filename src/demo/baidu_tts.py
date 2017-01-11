# coding: utf-8

import requests
import urllib.parse

URL_TTS = u'http://tts.baidu.com/text2audio?'
URL_TTS2 = u'http://fanyi.baidu.com/gettts?'
TARGET = r'../../res/out.mp3'

headers = {
    u'User-Agent': u'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; ) Gecko/20100101 Firefox/21.0'
}


def tts(text, lan='zh', sped='5'):
    """
    Convert text to MP3 audio with Baidu's TTS engine.
    :param text:
    :param lan: What language to be convert. Support zh(Chinese) and en(English)
    :param sped: Sound Speed
    :return:
    """
    data = {
        u'lan': lan,
        u'pid': 101,
        u'ie': u'UTF-8',
        u'spd': sped,
        u'text': text,
    }
    url = URL_TTS + urllib.parse.urlencode(data)
    response = requests.get(url, headers=headers)
    with open(TARGET, 'wb') as f:
        f.write(response.content)


def tts2(text, lan='zh', sped='5'):
    """
    Convert text to MP3 audio with Baidu's TTS engine.
    :param text:
    :param lan: What language to be convert. Support zh(Chinese) and en(English)
    :param sped: Sound Speed
    :return:
    """

    session = requests.Session()
    session.get('http://fanyi.baidu.com/')
    data = {
        u'lan': lan,
        u'spd': sped,
        u'text': text,
        u'source': u'web'
    }
    url = URL_TTS2 + urllib.parse.urlencode(data)
    response = session.get(url, headers=headers)
    with open(TARGET, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    tts2(u'这是一个中文测试文本')
