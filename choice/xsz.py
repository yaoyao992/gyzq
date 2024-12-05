import pandas as pd  
import xlrd
import openpyxl
import os
os.environ['PYDEVD_CONTAINER_RANDOM_ACCESS_MAX_ITEMS'] = '50000'

def  replace_xsz(gplist_xsl,xsz_xls): 
    # 读取Excel文件  
    df_excel_gplist = pd.read_excel(gplist_xsl,usecols=[0,1],engine='xlrd')  

    #df_excel.columns = ['id', 'ratio']  # 设置列名

    replace_dict_gplist = {} 
 


    for index, row in df_excel_gplist.iterrows():
        #循环生成字典
        print(row)
        id, name=str(row[0]),row[1]        
        replace_dict_gplist[id] = {'name': name}



 
    ##print("ok")




    workbook = openpyxl.load_workbook(xsz_xls) 
    worksheet=workbook['股票质押回购合约查询'] 
    for row in worksheet.iter_rows(min_row=2):
        id=row[6].value
        if id in  replace_dict_gplist:
            print("id in replace_dict_yg")
            replacements_gplist = replace_dict_gplist[id]
            row[7].value = replacements_gplist['name']
    
    workbook.save(xsz_xls)



replace_xsz('Y:/报表_于晓妮/GPLIST.xls','Y:/报表_于晓妮/股票质押回购合约查询2015年至今.xlsx')

