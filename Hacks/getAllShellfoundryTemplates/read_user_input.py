import json
import sys
import argparse


class parameter():
    def __init__(self, name, value):
        self.Name = name
        self.Value = value


class input_data(object):
    def __init__(self):
        creds = open(r'config_data.json', 'r')
        self.config_data = json.loads(creds.read())
        creds.close()

    def get_user_inputs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p","--path",
                            help="set path for saved templates")
        parser.add_argument("-t","--token",
                            help="set github token to use")
        args = parser.parse_args()
        # handle the input:
        if args.path:
            self.path = args.path
        else:
            print ("no path recieved! exiting")
            sys.exit(21)
