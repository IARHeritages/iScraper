import csv
import os


'''This is a class where data are loaded from a .csv file.
That file's data are then passed to the data object.
The data object is then used for analysis.'''
class LoadData:
    
    '''
    This instantiates the class with a reference to a file location (i.e., where a file is)
    @param fileLocation: The location of the file (i.e., its path''' 
    def __init__(self,fileLocation,driverLocation):
        self.fileLocation=fileLocation
        self.driverLocation=driverLocation
    
    '''
    This opens the file and puts the data in the appropriate places in the data file
    '''
    def runFile(self):
        
        #first, open the file and put into object f
        f = open(self.fileLocation, 'rU')
        self.rows=[]
        #We can use a try clause to read the file
        try:
            reader = csv.reader(f)
            i=0
            
            
            #for loop, skipping the first line (i.e., when i is 0)
            for row in reader:
                if(i==0):
                    i=i+1
                    continue
            
                self.rows.append(row)
               
        #then close the file
        finally:
            f.close()


#This is code executed outside the class but will call this and other classes

#This code changes the current directory so relative paths are used
os.chdir('../')
pn=os.path.abspath('../')

path=os.path.join(pn,'input','search.csv')
path2=os.path.join(pn,'input','meta_data')
f=open(path2)

ld=LoadData(path,f.readline())
ld.runFile()

sc=SeleniumScraper(ld.driverLocation,ld.rows)
sc.runScraper()


