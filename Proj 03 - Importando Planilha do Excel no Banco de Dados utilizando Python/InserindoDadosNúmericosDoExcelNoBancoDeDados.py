import pandas as pd
import mysql.connector

Sheetl_df = pd.read_excel("25112023InserindoDadosExcelNoBancoDeDados.xlsx")

conectar = mysql.connector.connect(host='localhost', user='root', password='1234', database='youtube')
cursor = conectar.cursor()

for index, row in Sheetl_df.iterrows():
    nome        = Sheetl_df.loc[index, "Nome"]
    email       = Sheetl_df.loc[index, "Email"]
    telefone    = Sheetl_df.loc[index, "Telefone"]
    doc         = Sheetl_df.loc[index, "Doc"]
    value  = Sheetl_df.loc[index, "Value"].astype(float)
    
    sql_query = f"INSERT INTO dantasdc (nome, email, telefone, doc, value) VALUES ('{nome}', '{email}', '{telefone}', '{doc}', '{value}')"
    cursor.execute(sql_query) 
   

conectar.commit()    

cursor.close() 
conectar.close() 