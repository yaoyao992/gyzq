import pandas as pd  
import dbfread 
import dbf 
import xlrd
import openpyxl
import filetype
from dbfpy3 import dbf

def  replace_SZ_radio(yuegaoxls_path,dbf_path): 
    # 读取Excel文件  
    df_excel = pd.read_excel(yuegaoxls_path,usecols=[1,6],engine='xlrd')  
    #df_excel.columns = ['id', 'ratio']  # 设置列名

    replace_dict = {} 

    print(df_excel)

    for index, row in df_excel.iterrows():
        #循环生成字典
        print(row)
        id, ratio=row[0],row[1]
        
        replace_dict[id] = {'ratio': ratio}

    with dbf.Dbf(dbf_path) as db:
        # print(db, '\n')
        for record in db:
            print(record, '\n')
            id=record[b'CSHTXH']
            if id in  replace_dict:
                replacements = replace_dict[id]                

                if record[b'LYBZBL'] <= record[b'PCX']:
                    print('yao')
                    record[b'LYBZJB'] = '2'    
                elif record[b'LYBZBL'] >= record[b'YJX']:        
                    record[b'LYBZJB'] = '0'
                else:   
                    record[b'LYBZJB'] = '1'   

                record[b'LYBZBL'] = round(replacements['ratio']*100)    

            db.write(record)


  


replace_SZ_radio('Y:/gpzy__20240423.xls','Y:/ZYHG0002_20240422.DBF')

