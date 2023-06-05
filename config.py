import configparser 
import os 

parser = configparser.ConfigParser() 
fullpath = os.path.expanduser("~/.config/whats-send.conf") 

def generate_conf():
    

    api_id = input("Enter your api id: ") 
    api_token = input("Enter your api token: ") 

    if api_id and api_token:

        parser['whats-send'] = {
                'api_id': api_id,
                'api_token': api_token, 
                } 

        with open(fullpath, 'w') as f: 
            parser.write(f) 
