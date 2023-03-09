import argparse
import os
import time
from code_splunker.splunk import splunk

banner = """
 _____           _        _____       _             _
/  __ \         | |      /  ___|     | |           | |
| /  \/ ___   __| | ___  \ `--. _ __ | |_   _ _ __ | | _____ _ __
| |    / _ \ / _` |/ _ \  `--. \ '_ \| | | | | '_ \| |/ / _ \ '__|
| \__/\ (_) | (_| |  __/ /\__/ / |_) | | |_| | | | |   <  __/ |
 \____/\___/ \__,_|\___| \____/| .__/|_|\__,_|_| |_|_|\_\___|_|
                               | |
                               |_|                                """
def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise NotADirectoryError(string)

def main():
    parser = argparse.ArgumentParser(description = 'Locate code caves within a program')
    parser.add_argument('-f','--file', required=True,help='File to look for codecaves')
    parser.add_argument('-s','--size',type=int , required = True, help='Minimum size of cave to look for')
    args = parser.parse_args()
    file_path(args.file)
    if args.size >= 0:
        pass
    else:
        raise ValueError("Minimum cave size was be greater or equal to 0!")
    print(banner)
    print('[*] Starting the code splunking process...')
    print(" ")
    time.sleep(2)
    splunk(args.file,args.size)
    print('[*] Splunking complete!')

if __name__ == "__main__":
    main()
