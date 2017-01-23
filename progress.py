import argparse
import json
import os
import subprocess
from datetime import datetime

import tweepy


def word_count(file):
    basedir = os.path.dirname(file)
    count = subprocess.check_output(
        'cd {} ; detex {} | wc -m'.format(basedir, file), shell=True)
    count = int(count.strip())
    return count


def progbar(p, length=20):
    fin = int(min(p, 1) * length)

    faces = ['orz', '(´;ω;`)', '(๑¯ω¯๑)', '(*´﹃｀*)', '٩(ˊᗜˋ*)و']
    face = faces[int(p * 4)]
    return '{face} [{bar:-<{length}}] {p:2.0%}'.format(p=p, bar='#' * fin,
                                                       length=length, face=face)


def message(count, goal):
    deadline = datetime.strptime('17-02-13 15:00:00', '%y-%m-%d %H:%M:%S')
    delta = deadline - datetime.now()

    return """そつろんをかこう！
進捗 {}字
目標 {}字
残り {}日

{}
""".format(count, goal, delta.days, progbar(count / goal))


def tweet(message, setting):
    auth = tweepy.OAuthHandler(setting['consumer_key'],
                               setting['consumer_token'])
    auth.set_access_token(setting['token'], setting['secret'])
    api = tweepy.API(auth)
    api.update_status(status=message)
    print('tweeted!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Progress Bot')
    parser.add_argument('file', metavar='FILE', type=str, help='latex file')
    parser.add_argument('-g', '--goal', default=20000, type=int,
                        help='Goal (default: 20000)')
    parser.add_argument('-s', '--setting', default='setting.json', type=str,
                        help='Setting file name (default: setting.json)')
    args = parser.parse_args()

    with open(args.setting, 'r') as f:
        setting = json.load(f)

    count = word_count(os.path.abspath(args.file))
    tweet(message(count, args.goal), setting)
