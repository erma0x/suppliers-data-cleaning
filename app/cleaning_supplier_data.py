#!/usr/bin/python
import sys, getopt
import numpy as np
import pandas as pd
from suppliers_names import suppliers
from dataclasses import dataclass
from pathlib import Path
import argparse
import getopt

@dataclass
class Fornitore():

    input_file_path: str = ''
    
    def process_date(self):
        pass
    
    def load_csv(self):
        pass



@dataclass
class Yakima(Fornitore):

    input_file_path: str = 'suppliers_data/yakima_adjusted.csv'
    output_file_path:str = 'suppliers_data/yakima_NEW.csv'
    
    def set_input_file_path(self, file_input_path):
        self.input_file_path =  file_input_path 

    def set_output_file_path(self, file_output_path):
        self.output_file_path =  file_output_path 

    def get_input_file_path(self):
        return self.input_file_path 

    def get_output_file_path(self):
        return self.output_file_path 
    

    def process_datetime(self, date_colum_name='Anno'):
        """ reformat strange datetime 
            
        examples:    
            FROM   a)   12/90>
                   b)   2/92>4/06  
            TO
                   a)   1990-
                   b)   1992-2006
        """
        dataframe=self.load_csv()
        
        df_adjusted_dates = dataframe[date_colum_name].copy()

        for i in range(len(df_adjusted_dates)):

            list_of_dates = df_adjusted_dates[i].split('>')
            
            for j in range(len(list_of_dates)):
                if len(list_of_dates[j])>1: # if date exist
                    list_of_dates[j]=list_of_dates[j][3:5] # take only year number
                    if list_of_dates[j][0] in ('6789'): # 1999 or less  # from 1960 to 1999
                        list_of_dates[j]='19'+list_of_dates[j] # ex. 90 into 1990
                    else:                        # 2000 or more
                        list_of_dates[j]='20'+list_of_dates[j] # ex. 06 into 2006
                        
            df_adjusted_dates[i]='-'.join(list_of_dates)
            
        dataframe[date_colum_name] = df_adjusted_dates
        return dataframe
    
    def load_csv(self):
        df = pd.read_csv(self.input_file_path, sep=',')
        return df



        
class Pirelli(Fornitore):
    
    def __init__(self):
        pass
    
    def process_date(self):
        pass
    
    def load_csv(self):
        pass
    
def main(argv):
#def main():
    """
    PULIZIA DATI DEI FORNITORI
        polimorfismo di classi
        ogni fornitore ha gli stessi metodi
        per preprocessare i dati, ma ogni fornitore
        ha caratterstiche diverse, quindi fra di loro i metodi
        dei fornitori avranno diversi variazioni.

    TERMINALE  
        usage: .py -i <inputfile> -o <outputfile>
        python3 -f [id] -i [.csv] -o [.csv] -d 
    -s --supplier:       supplier id or name (1:'yamaha')
    -i --input-csv:     .csv file name 
    -o --output-csv:    .csv file name
    -d --date:          default=False, se True processa le date

    """
    inputfile = ''
    outputfile = ''
    
    #parser = argparse.ArgumentParser()
    #parser.parse_args()

    
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "s:i:o:")

    except getopt.GetoptError:
        print(main.__doc__)
        sys.exit(2)
        
    for opt, arg in opts: # search options
        #if opt in ['-h','--help']: 
        #    print(main.__doc__)
        #    sys.exit()

        if opt in ["-s"]:#, "--supplier"]: 
            supplier = arg
            
        elif opt in ["-i"]:#, "--input-file"]: 
            inputfile = arg
        
        elif opt in ["-o"]:#, "--output-file"]:
            outputfile = arg
        
        else:
            usage()
            sys.exit(2)        
    
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)
    

    if supplier in ('yakima','YAKIMA','0'):
        fornitore_yakima = Yakima()
        fornitore_yakima.set_input_file_path(inputfile)#sys.path[0]+'/suppliers_data/yakima_adjusted.csv')
        fornitore_yakima.set_output_file_path(outputfile)#sys.path[0]+'/suppliers_data/yakima_NEW.csv')
        fornitore_yakima.process_datetime().to_csv(fornitore_yakima.get_output_file_path())
    
    
    elif supplier in ('greenvalley','GREENVALLEY','1'): 
        pass
        
    else:
        print('please specify the suppliers with the option -s or --suppliers')

    
if __name__ == "__main__":
    main(sys.argv[1:])
    #main()