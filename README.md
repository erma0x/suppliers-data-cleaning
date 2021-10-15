# Cleaning suppliers data

### Enviroment Installation

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. pyhton3 app/clean_suppliers_data.py

## General usage
python3 app/cleaning_suppliers_data.py -s <supplier-name> -i <csv-input-file> -o <csv-output-file>

## Example usage 
python3 app/cleaning_supplier_data.py -s yakima -i /home/moebius/Desktop/cleaning_suppliers_data/app/suppliers_data/yakima_adjusted.csv -o /home/moebius/Desktop/cleaning_suppliers_data/app/suppliers_data/yakima_NEEEW.csv

