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

def parse_args():
    parser = argparse.ArgumentParser(description='check_url_status')

    parser.add_argument(
        '-fi',
        dest='file_in',
        type=str,
        default='file_in.txt',
        help='file name in'
    )
    parser.add_argument(
        '-fo',
        dest='file_out',
        type=str,
        default='file_out.txt',
        help='file name out'
    )
    return parser.parse_args()

def write_file(file_out, data):
    file_o = open(file_out, "a")
    file_o.write(data + '\n')


if __name__ == '__main__':
    args = parse_args()
    file_in = args.file_in
    file_out = args.file_out

    list_url = read_file(file_in)

    file_o = open(file_out, "w")
    for url in list_url:
        url = url.rstrip()
        code = get_code(url)
        data = "{},{}".format(url, code)
        print(data)
        write_file(file_out, data)


