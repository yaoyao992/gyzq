import os
import sys 

def replace_zyhg_ratio(zyhgfile,dir,replacefile):
    replace_dict = {}  
  
    # 从replace.txt中读取替换规则  
    with open(replacefile, 'r') as f:  
        for line in f:  
            code, ratio, flag = line.strip().split()  # 假设值之间由空格分隔  
            replace_dict[code] = {'ratio': ratio, 'flag': flag}  
  
    # 读取zhyg.txt，替换retio，并写入临时文件  
    temp_filename = os.path.join(dir, "zhyg_temp.txt")
    with open(zyhgfile, 'r', newline='') as zhyg_file, open(temp_filename, 'w', newline='') as temp_file:  
        for line in zhyg_file:  
            columns = line.strip().split("|")  # 假设列之间由空格分隔  
    
            code_value = columns[7]  # 第5列是code  
           
                
            if code_value in replace_dict:  
                replacements = replace_dict[code_value]   #将三维的字典，转化成二维的字典
                if replacements['ratio']=="unchanged":    #如果ratio是unchanged，则只改变flag的值                  
                    columns[23] = replacements['flag'].rjust(1)
                else:                      
                    columns[22] = replacements['ratio'].rjust(9) 
                    columns[23] = replacements['flag'].rjust(1)
            temp_file.write('|'.join(columns) + " "*100 + '\n')  
  
   
  
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
        dir=sys.argv[2] 
        replacefile=sys.argv[3]  
           
    else:
        print("参数输入错误")
    
    replace_zyhg_ratio(zyhgfile,dir,replacefile)


if __name__ == "__main__":
    main()


