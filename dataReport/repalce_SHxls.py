import os
import sys 
import pandas as pd  
import dbf 
from dbfpy3 import dbf

def replace_zyhg_ratio(zyhgfile,dir,ygfile,cwline):
    replace_ratio_dict = {}  
    replace_line_dict = {}  
    
    df_ration = pd.read_excel(ygfile,usecols=[1,6],engine='xlrd')
    df_cw = pd.read_excel(cwline,usecols=[0,4,5,6],engine='xlrd')
    for index, row in df_ration.iterrows():
        #循环生成字典
        print(row)
        id, ratio=str(row[0]).split('.')[0] ,row[1]
        replace_ratio_dict[id] = {'ratio': ratio}  
    
    for index, row in df_cw.iterrows():
        #循环生成字典
        print(row)
        id, wline,cline,name=str(row[0]).split('.')[0],row[1],row[2],str(row[3])
        replace_line_dict[id] = {'wline': wline,'cline':cline,'name':name}  
    
    

  
    # 读取zhyg.txt，替换retio，并写入临时文件  
    temp_filename = os.path.join(dir, "zhyg_temp.txt")
    with open(zyhgfile, 'r', newline='') as zhyg_file, open(temp_filename, 'w', newline='') as temp_file:  
        for line in zhyg_file:  
            columns = line.strip().split("|")  # 假设列之间由空格分隔  
    
            id = columns[4].strip() # 第5列是code  
           
                
            if id in replace_ratio_dict:  
                replacement_ratio = replace_ratio_dict[id]   #将三维的字典，转化成二维的字典
                columns[22] = round(replacement_ratio['ratio'],4)


            if id in replace_line_dict: 
                replacement_line = replace_line_dict[id]
                columns[8] = replacement_line['name']
                if columns[22] >= replacement_line['wline']:
                    columns[23] = 0
                elif columns[22] < replacement_line['cline']:
                    columns[23] = 2
                else:
                    columns[23] = 1
    
            columns[8] = columns[8].rjust(4)
            if id in replace_ratio_dict:  
                columns[22]=str("{:.2f}".format((columns[22]*100))).rjust(9)
            columns[23]=str(columns[23]).rjust(1)


            temp_file.write('|'.join(columns) + " "*100 + '\n')  
  
    print("SH files have processed")
  
     # 用临时文件替换原文件  
    try:  
        os.replace(temp_filename, zyhgfile)  
    except OSError:  
        # 如果在不同驱动器或文件系统上，尝试先删除原文件再重命名  
        os.remove(zyhgfile)  
        os.rename(temp_filename, zyhgfile)  

#replace_zyhg_ratio('D:/data/postModify/zyhg0065100120240410.txt','D:/data/postModify','D:/data/postModify/replace.txt')

def main():
    if len(sys.argv) > 1:
        zyhgfile = sys.argv[1]
        dir =  sys.argv[2]
        ygfile=sys.argv[3] 
        cwline=sys.argv[4]  
           
    else:
        print("参数输入错误")
    
    replace_zyhg_ratio(zyhgfile,dir,ygfile,cwline)

    #replace_zyhg_ratio('D:/data/zyhg0065100120241022.txt','D:/data/','D:/data/zyds.xls','D:/data/cw_line.xls')


if __name__ == "__main__":
    main()


