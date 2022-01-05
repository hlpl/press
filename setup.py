#! /usr/bin/python 
from setuptools  import setup
import os
import sys
import platform
import configparser

from io import open
# to install type:
# python setup.py install --root=/
LONG_DESCRIPTION=open('README.md','r',encoding='utf8').read()        
        
if sys.version_info[0] < 3:
    raise Exception(
        'You are tying to install hlpl_press on Python version {}.\n'
        'Please install hlpl_press in Python 3 instead.'.format(
            platform.python_version()
        )
    )
    
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'hlpl_press/setup.cfg')
config.read(config_file_path)

VERSION = config['hlpl_press']['version']
AUTHOR = config['hlpl_press']['author']
AUTHOR_EMAIL = config['hlpl_press']['email']
URL = config['hlpl_press']['url']


projects_urls={}
for i in range(4,len(list(config['hlpl_press'].keys()))):
    x=list(config['hlpl_press'].keys())[i]
    y=x
    if i>3:
       y=y[0:len(y)-4]
    projects_urls[y]=config['hlpl_press'][x]
    

setup (name='hlpl_press', version=VERSION,
      description='hlpl_press is a web designer (or site duilder) using python as core engine.',
      long_description_content_type='text/markdown',  
      long_description = LONG_DESCRIPTION,       
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=URL+'/download/',
      project_urls=projects_urls,      
      python_requires='>=3, <=3.9',
      license='MIT',
      platform="OS independent",
      keywords=['hlpl_press', 'hlpl press', 'hlpl-press', 'web designer', 'website', 'hlpl'],
      package_dir={'hlpl_press': 'hlpl_press',},
      packages=['hlpl_press',],
      install_requires=[],         
      include_package_data=True,
      entry_points ={
        'console_scripts': [
                'hlpl_press = hlpl_press.__main__:main',
            ]},   
      classifiers=[
          'Environment :: Web Environment',
          ],
                  
    );
