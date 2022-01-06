
import configparser
import sys
import os

def get_hlpl_press_version(case):
    config = configparser.ConfigParser()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, 'setup.cfg')
    config.read(config_file_path)
    if case=='version':
       return config['hlpl_press']['version']
    if case=='else':
       return config['hlpl_press']['version']+'\n'+config['hlpl_press']['author']+'\n'+config['hlpl_press']['email']+'\n'+config['hlpl_press']['url']+'\n'
       
 
    
def main():
    if 'version' in sys.argv:
        print('\n'+get_hlpl_press_version('version'))
    else:
        print('\n'+get_hlpl_press_version('else')+'\n'+'hlpl_press under developement, it will be released next versions of HLPL')