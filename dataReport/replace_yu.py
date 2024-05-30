import pandas as pd  
import xlrd
import openpyxl

def  replace_SZ_radio(yxn_xlsx,xone_xls,yuegao_xls): 
    # 读取Excel文件  
    df_excel_yg = pd.read_excel(yuegao_xls,usecols=[1,6],engine='xlrd')  
    df_excel_xone = pd.read_excel(xone_xls,usecols=[3,29],engine='xlrd')  
    #df_excel.columns = ['id', 'ratio']  # 设置列名

    replace_dict_yg = {} 
    replace_dict_xone = {} 
    print(df_excel_yg)
    # **********************************
    print(df_excel_xone)


    for index, row in df_excel_yg.iterrows():
        #循环生成字典
        print(row)
        id, ratio=str(row[0]),row[1]        
        replace_dict_yg[id] = {'ratio_yg': ratio}

    for index, row in df_excel_xone.iterrows():
        #循环生成字典
        print(row)
        id, ratio=str(row[0]),row[1]      
        replace_dict_xone[id] = {'ratio_xone': ratio}
    

 
    print("ok")




    workbook = openpyxl.load_workbook(yxn_xlsx) 
    worksheet=workbook['自有资金合约'] 
    for row in worksheet.iter_rows(min_row=2):
        id=row[15].value
        if id in  replace_dict_yg:
            print("id in replace_dict_yg")
            replacements_yg = replace_dict_yg[id]
            row[11].value = replacements_yg['ratio_yg']
        if  id in  replace_dict_xone:
            print("id in replace_dict_xone")
            replacements_xone = replace_dict_xone[id]
            row[12].value = replacements_xone['ratio_xone']
    
    worksheet=workbook['资管纾困计划（自有出资）合约'] 
    for row in worksheet.iter_rows(min_row=2):
        id=row[15].value
        if id in  replace_dict_yg:
            print("id in replace_dict_yg")
            replacements_yg = replace_dict_yg[id]
            row[11].value = replacements_yg['ratio_yg']
        if  id in  replace_dict_xone:
            print("id in replace_dict_xone")
            replacements_xone = replace_dict_xone[id]
            row[12].value = replacements_xone['ratio_xone']    
        print(row[2])
        print("ok")
    
    worksheet=workbook['违约项目（自有资金合约）'] 
    for row in worksheet.iter_rows(min_row=2):
        id=row[15].value
        if id in  replace_dict_yg:
            print("id in replace_dict_yg")
            replacements_yg = replace_dict_yg[id]
            row[11].value = replacements_yg['ratio_yg']
        if  id in  replace_dict_xone:
            print("id in replace_dict_xone")
            replacements_xone = replace_dict_xone[id]
            row[12].value = replacements_xone['ratio_xone']    

    workbook.save(yxn_xlsx)




replace_SZ_radio('Y:/股票质押回购合约明细0524.xlsx','Y:/股票质押履约比例查询240524.xls','Y:/yugao_20240528.xls')

