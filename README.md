# Suppliers Data Cleaning

Scripts for processing data through data classes for suppliers that are managed separately. Through the data of classes with polymorphism it is possible to modify, add, and easily handle the different types of formatting that the supplier sends in .csv 

### Installation
1. Create the virtual enviroement
``` python
python3 -m venv venv
```

2. Activate the virtual enviroement
``` python
source venv/bin/activate
```
3. Install the requirements
``` python
pip install -r requirements.txt
```

4. Lunch the script
``` python
pyhton3 app/suppliers-data-cleaning.py -s <supplier> -i <input file> -o <output file>
```  
  
### Usage
``` python
python3 app/suppliers-data-cleaning.py -s supplier -i /home/user/Desktop/cleaning_suppliers_data/app/suppliers_data/yakima_input.csv -o /home/user/Desktop/cleaning_suppliers_data/app/suppliers_data/yakima_output.csv
```
