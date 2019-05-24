#!/usr/bin/env python3

import os
import re
import getpass
import configparser
import argparse

split_token = re.escape("/")

parser = argparse.ArgumentParser()
parser.add_argument("pwd", nargs='?', default=os.getcwd(), help="The path to shorten.")
args = parser.parse_args()
pwd = args.pwd

config = configparser.ConfigParser()
config['settings'] = {
    'break_length': '5',
    'keep_length': '3',
    'replacement': '+'
}
config.read(['config.ini', os.path.expanduser('~/.config/pwd-shorten/config.ini')])
break_length = config.getint('settings', 'break_length')
keep_length = config.getint('settings', 'keep_length')
replacement = config['settings']['replacement']

# replacements
home_pattern = re.escape("/home/" + getpass.getuser())
source_pattern = re.escape("/source/src")
windows_home_pattern = re.escape("/mnt/c/Users")

# Do replacements to the full path
pwd = re.sub(home_pattern, "~", pwd)
pwd = re.sub(source_pattern, "/~", pwd)
pwd = re.sub(windows_home_pattern, "w~", pwd)

# evaluate each directory in path and shorten accordingly
pwd = re.split(split_token, pwd)
for index in range(0, len(pwd) - 1):
    if len(pwd[index]) > break_length:
        pwd[index] = pwd[index][:keep_length] + replacement

print('/'.join(pwd))
