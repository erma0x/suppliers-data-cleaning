#!/usr/bin/python
import sys, getopt
import pandas as pd
#import numpy as np
from suppliers_names import suppliers

class Fornitore():
    
    def __init__(self):
        pass

    def process_date(self):
        pass
    
    def load_csv(self):
        pass

class Yamaha(Fornitore):
    
    def __init__(self):
        pass

    def process_date(self):
        pass
    
    def load_csv(self):
        pass
    
class Pirelli(Fornitore):
    
    def __init__(self):
        pass
    
    def process_date(self):
        pass
    
    def load_csv(self):
        pass
    
def main(argv):
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
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      
    except getopt.GetoptError:
        print(main.__doc__)
        sys.exit(2)
        
    for opt, arg in opts: # search options
        if opt == '-h' or opt=='--help': # request help
            print(main.__doc__)
            sys.exit()

        elif opt in ("-s", "--supplier"): # input file
            supplier = arg
            
        elif opt in ("-i", "--input-csv"): # input file
            inputfile = arg
        
        elif opt in ("-o", "--output-csv"):
            outputfile = arg
        
        #elif opt in ('-d','--date'):
        #    my_file = pd.read_csv(inputfile)
         #   outputfile = pd.save_csv()
        else:
            pass
        
    else:
        print(main.__doc__)
        
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)
    if supplier in (1)

if __name__ == "__main__":
    main(sys.argv[1:])
