import os
import pandas as pd
import math

nombres = list()
totales = list()
#Scan the current directory for excel files
basepath = '.'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)) and entry.endswith('.xlsx'):
         excelFile = pd.read_excel(entry)
         for index, row in excelFile.iterrows():
         	 nombres.append(row.Nombre)
         	 totales.append(0 if math.isnan(row.Total) else row.Total)
         	
# Creates and save the new excel
data = {
	'Nombres' : nombres,
	'Totales' : totales
}
newExcel = pd.DataFrame(data)
newExcel.to_excel('ExcelConverted.xlsx')