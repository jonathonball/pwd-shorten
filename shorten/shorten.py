import os
import re
import argparse
import configparser
import getpass

class Shorten:
    """directory shortener for bash and zsh $PS1 prompts."""

    def __init__(self, args):
        """Sets up for and shortens a filesystem path
        args:
            args -- The command line arguments provided to this application"""
        self.setup_regex_escaping()
        self.setup_from_configparser()
        self.setup_from_argparse(args)
        self.sub_replacements_on_whole_path()
        self.sub_replacements_on_dir_names()
        print(self.pwd)

    def setup_from_configparser(self):
        """Sets our defaults from configparser, if any"""
        self.config = configparser.ConfigParser()
        self.config['settings'] = {
            'break_length': '5',
            'keep_length': '3',
            'replacement': '+'
        }
        self.config.read(['config.ini', os.path.expanduser('~/.config/pwd-shorten/config.ini')])
        self.break_length = self.config.getint('settings', 'break_length')
        self.keep_length = self.config.getint('settings', 'keep_length')
        self.replacement = self.config['settings']['replacement']

    def setup_regex_escaping(self):
        """Properly escapes select strings so they can be used in a regex without manually doing it"""
        self.split_token = re.escape("/")
        self.home_pattern = re.escape("/home/" + getpass.getuser())
        self.source_pattern = re.escape("/source/src")
        self.windows_home_pattern = re.escape("/mnt/c/Users")

    def setup_from_argparse(self, args):
        """Set parameters passed in on the command line as arguments
        args:
            args -- The command line arguments provided to this application"""
        parser = argparse.ArgumentParser(args)
        parser.add_argument("pwd", nargs='?', default=os.getcwd(), help="The path to shorten.")
        self.args = parser.parse_args()
        self.pwd = self.args.pwd

    def sub_replacements_on_whole_path(self):
        """Perform global replacements on the entire path string"""
        pwd = re.sub(self.home_pattern, "~", self.pwd)
        pwd = re.sub(self.source_pattern, "/~", pwd)
        pwd = re.sub(self.windows_home_pattern, "w~", pwd)
        self.pwd = pwd

    def sub_replacements_on_dir_names(self):
        """Break the pwd into its directory parts and do replacements for each part"""
        pwd = re.split(self.split_token, self.pwd)
        for index in range(0, len(pwd) - 1):
            if len(pwd[index]) > self.break_length:
                pwd[index] = pwd[index][:self.keep_length] + self.replacement
        self.pwd = '/'.join(pwd)
