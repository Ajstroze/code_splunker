import argparse
import os
from .splunk import splunk

banner = """
 _____           _        _____       _             _
/  __ \         | |      /  ___|     | |           | |
| /  \/ ___   __| | ___  \ `--. _ __ | |_   _ _ __ | | _____ _ __
| |    / _ \ / _` |/ _ \  `--. \ '_ \| | | | | '_ \| |/ / _ \ '__|
| \__/\ (_) | (_| |  __/ /\__/ / |_) | | |_| | | | |   <  __/ |
 \____/\___/ \__,_|\___| \____/| .__/|_|\__,_|_| |_|_|\_\___|_|
                               | |
                               |_|                                """
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def main():
    parser = argparse.ArgumentParser(description = 'Locate code caves within a program')
    parser.add_argument('-f','--file', type=dir_path, required=True,help='File to look for codecaves')
    parser.add_argument('-s','--size',type=int , required = True, help='Minimum size of cave to look for')
    args = parser.parse_args()
    try:
        args.size >= 0
    except ValueError:
        print("Minimum cave size was be greater or equal to 0!")
        return -1
    print(banner)
    print('[*] Starting the code splunking process...')
    splunk(args.file,args.size)

if __name__ == "__main__":
    main()
