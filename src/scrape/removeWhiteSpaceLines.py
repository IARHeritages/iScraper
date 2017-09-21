'''
Created on Jun 7, 2017

@author: maltaweel
'''

import os
import re
os.chdir('../')
fileLocation=os.path.abspath('../')
path=fileLocation+'/output/'

for filename in os.listdir(path):
    with open(path+filename, 'r') as filehandle:
        lines = filehandle.readlines()
        with open(path+filename, 'w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            
            for f in lines:
        
                if f=='",,,,,':
                    lines.remove(f)
               
            filehandle.writelines(lines)   


