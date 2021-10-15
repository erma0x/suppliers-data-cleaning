#!/usr/bin/python
import sys,getopt 
import pandas as pd
from dataclasses import dataclass

#projct modules
from suppliers_names import suppliers


@dataclass
class Supplier():

    input_file_path: str = ''
    output_file_path: str = ''

    def set_input_file_path(self, file_input_path):
        self.input_file_path =  file_input_path 

    def set_output_file_path(self, file_output_path):
        self.output_file_path =  file_output_path 

    def get_input_file_path(self):
        return self.input_file_path 

    def get_output_file_path(self):
        return self.output_file_path 
        
    def process_date(self):
        print('ERROR: process date not configured')
    
    def load_csv(self):
        print('ERROR: load csv not configured')


@dataclass
class Yakima(Supplier):

    input_file_path: str = 'app/suppliers_data/yakima_adjusted.csv'
    output_file_path:str = 'app/suppliers_data/yakima_NEW.csv'
        
    def process_datetime(self, dataframe, date_colum_name='Anno'):
        """ reformat strange datetime 
            
        examples:    
            FROM   a)   12/90>
                   b)   2/92>4/06  
            TO
                   a)   1990-
                   b)   1992-2006
        """
        

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
    
    def remove_inside_brakets(self,dataframe,column_name='Modello'):
        import re
        mock_df = dataframe.copy()
        for i in range(len(mock_df)):
           string_before = dataframe[column_name][i]
           string_after = re.sub("[\(\[].*?[\)\]]", "", string_before)
           dataframe[column_name][i]=string_after
        return dataframe
        
class Greenvalley(Supplier):
    
    input_file_path: str = 'app/suppliers_data/greenvalley_aurilis_adjusted.csv.csv'
    output_file_path:str = 'app/suppliers_data/greenvalley_aurilis_NEW.csv'
    
    def process_datetime(self, dataframe, date_colum_name='Anno',date_colum_name2='Anno2'):
        """ reformat strange datetime 
        """
        
        df_anno1 = dataframe[date_colum_name].copy().astype(str).str.replace("\.0", "")
        df_anno2 = dataframe[date_colum_name2].copy().astype(str).str.replace("\.0", "") 
        dataframe[date_colum_name] = df_anno1+'-'+df_anno2
        del dataframe[date_colum_name2]
        
        return dataframe
    
    
    def load_csv(self):
        df = pd.read_csv(self.input_file_path, sep=',')
        return df
    
    def remove_inside_brakets(self,dataframe,column_name='Vettura'):
        import re
        mock_df = dataframe.copy()
        for i in range(len(mock_df)):
           string_before = dataframe[column_name][i]
           string_after = re.sub("[\(\[].*?[\)\]]", "", string_before)
           dataframe[column_name][i]=string_after
        return dataframe
    
def main(argv):
    """
    PULIZIA DATI DEI FORNITORI
        polimorfismo di classi
        ogni supplier ha gli stessi metodi
        per preprocessare i dati, ma ogni supplier
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
    
    inputfile = ''  # your default values
    outputfile = ''
    
    
    # Get the CLI argouments
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "s:i:o:")

    except getopt.GetoptError:
        print(main.__doc__)
        sys.exit(2)
        
    for opt, arg in opts: # search options

        if opt in ["-s"]:#, "--supplier"]: 
            supplier = arg
            
        elif opt in ["-i"]:#, "--input-file"]: 
            inputfile = arg
        
        elif opt in ["-o"]:#, "--output-file"]:
            outputfile = arg
        
        else:
            usage()
            sys.exit(2)        

    print('Supplier choosen ',supplier)    
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)

    if supplier in ('yakima','YAKIMA','0'):
        
        supplier_yakima = Yakima()
        supplier_yakima.set_input_file_path(inputfile)        
        supplier_yakima.set_output_file_path(outputfile)       
        
        df_yakima=supplier_yakima.load_csv() #read csv
        
        df_yakima.pipe(supplier_yakima.process_datetime) #pipeline
        
        df_yakima.to_csv(supplier_yakima.get_output_file_path(),sep='\t') #save csv

    
    elif supplier in ('greenvalley','GREENVALLEY','1'): 
        
        supplier_greenvalley = Greenvalley()
        supplier_greenvalley.set_input_file_path(inputfile)        
        supplier_greenvalley.set_output_file_path(outputfile)
        
        df_greenvalley = supplier_greenvalley.load_csv() #read csv

        df_greenvalley.pipe(supplier_greenvalley.process_datetime).pipe(supplier_greenvalley.remove_inside_brakets) #pipeline
        
        df_greenvalley.to_csv(supplier_greenvalley.get_output_file_path(),sep='\t') #save csv
        
        
    else:
        print('please specify the suppliers with the option -s or --suppliers')

    
if __name__ == "__main__":
    main(sys.argv[1:])
