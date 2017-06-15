'''
Created on Jun 7, 2017

@author: maltaweel
'''

import os

os.chdir('../')
fileLocation=os.path.abspath('../')
path=fileLocation+'/tweets/'

for filename in os.listdir(path):
    with open(path+filename, 'r') as filehandle:
        lines = filehandle.readlines()
        with open(path+filename, 'w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            filehandle.writelines(lines)   
        