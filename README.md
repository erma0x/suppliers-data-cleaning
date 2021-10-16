# Suppliers Data Cleaning

Scripts for processing data through data classes for suppliers that are managed separately. Through the data of classes with polymorphism it is possible to modify, add, and easily handle the different types of formatting that the supplier sends in .csv 

### Installation
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- pyhton3 app/suppliers-data-cleaning.py -s <supplier> -i <input file> -o <output file>
  
### Usage
  
python3 app/suppliers-data-cleaning.py -s yakima -i /home/moebius/Desktop/cleaning_suppliers_data/app/suppliers_data/yakima_adjusted.csv -o /home/moebius/Desktop/cleaning_suppliers_data/app/suppliers_data/yakima_NEEEW.csv
