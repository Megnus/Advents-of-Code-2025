import re
import os
import sys
import requests

session = ('53616c7465645f5fb41b5e0a6cd31137596bc68d1085d2a37c3d2eb7'
           'a02591389d9bbb80fece36094e1f2d15660c4737d813267d1372267a0204aec8e1a8a331')


def test_data():
    day = re.findall(r'\d+', os.path.basename(sys.argv[0]))[0]
    file = 'input/day_{}.txt'.format(day)
    f = open(file, 'r')
    in_data = f.read()
    f.close()
    lines = in_data.splitlines()
    return lines


def puzzle_data():
    day = int(re.findall(r'\d+', os.path.basename(sys.argv[0]))[0])
    url = 'https://adventofcode.com/2025/day/{}/input'.format(day)
    cookies = {'session': session}
    response = requests.post(url, cookies=cookies)
    raw = response.content.decode("utf-8")
    lines = raw.splitlines()
    return lines


def get_data(test=False):
    return puzzle_data() if test else test_data()


def main():
    test_data()