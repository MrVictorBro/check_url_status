import requests
import argparse


def read_file(file_name):
    try:
        with open(file_name, "r") as myfile:
            data = myfile.readlines()
            return data
    except Exception as e:
        print(e)
        return ""

def get_code(url,headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64)'}):
    try:
        code_status = requests.get(url).status_code
        return code_status
    except Exception as e:
        print(e)
        return ""

def get_url(data):
    for url in data:
        url = url.rstrip()
        code = get_code(url)
        print(url, code)

def parse_args():
    parser = argparse.ArgumentParser(description='check_url_status')

    parser.add_argument(
        '-f',
        dest='file',
        type=str,
        default='file0.txt',
        help='file name'
    )
    return parser.parse_args()


if __name__ == '__main__':
    # file_name = 'file.txt'

    args = parse_args()
    file_name = args.file

    list_url = read_file(file_name)
    get_url(list_url)

