import os
import sys 

def replace_zyhg_ratio(zyhgfile,dir):
    
    with open(zyhgfile, 'r', newline='') as zhyg_file:
        for line in zhyg_file:  
            columns = line.split("|")  # 假设列之间由空格分隔  
    
          
            zhyg_file.write('|'.join(columns) + " "*100 + '\n')  
  


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