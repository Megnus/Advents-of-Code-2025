import re
import os
import sys
import requests

session = ('53616c7465645f5f01770bd62ec4f8d14a9bf8395ced3b77fd333d5066395ba1118'
           '9961da4f5fb02bc2954c4acfd1ca7c6c502fb548c7d271ec2bbc2f4e81669')


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