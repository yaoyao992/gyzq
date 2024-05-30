import datetime
import hashlib
import os
import time  
import logging  
import sys


  
  
def get_file_md5(file_path):  
    if not os.path.isfile(file_path):  
        return "File not found"  
  
    # 创建一个md5对象  
    md5 = hashlib.md5()  
  
    # 打开文件，并一块一块的读取文件内容  
    with open(file_path, "rb") as f:  
        for chunk in iter(lambda: f.read(4096), b""):  
            md5.update(chunk)  
  
    # 获取16进制摘要值  
    return md5.hexdigest().upper()  


def get_last_time(file_path,dt):  
    # 检查文件是否存在  
    if not os.path.isfile(file_path):  
        return "File not found"  
  
    # 获取文件的最后修改时间戳  
    last_modified_time = os.stat(file_path).st_mtime  
    #将时间戳分别转化为日期和时分秒
    last_modified_time_day = time.strftime('%Y%m%d', time.localtime(last_modified_time))
    last_modified_time_hms = time.strftime('%H%M%S', time.localtime(last_modified_time))
    # 将时间戳转换为人类可读的格式  
    if dt=='day':
        return last_modified_time_day
    else:
        return last_modified_time_hms

def get_file_size(file_path):  
    # 检查文件是否存在  
    if not os.path.isfile(file_path):  
        return "File not found"  
  
    # 获取文件大小（字节）  
    file_size = os.path.getsize(file_path)  
  
    # 如果需要，可以将文件大小转换为更易读的格式（例如KB, MB等）  
  
    return str(file_size)  


def get_file_path(dir,filename):
    # 获取当前日期  
#    today = datetime.date.today()  
  
    # 格式化日期为字符串  
#    formatted_date = today.strftime("%Y%m%d")  
  
   
#    if gzstr=='zyhgtxt':      
        # 定义路径模板  
        # 使用{}作为占位符，然后在调用format方法时传入相应的参数来替换这些占位符
#        path_template = "{dir}/zyhg00651001{date}.txt"   
        # 使用format方法将日期插入到路径模板中  
#    elif gzstr=='zyhgflg':
#        path_template = "{dir}/zyhg00651001{date}.flg"
#    elif gzstr=='zxbsrar': 
#        path_template = "{dir}/zxbs39018{date}001.rar"   
#    elif gzstr=='zxbsflg':
#        path_template = "{dir}/zxbs39018{date}001.flg"
#    else:
#        message ="入参为: "+dir+"   "+gzstr+"is not right"
#        raise ValueError(message)

#    path = path_template.format(date=formatted_date,dir=dir) 
    path=dir+filename
    return path

def get_file_name(file_path):
    # 打开文件并读取内容
    
    with open(file_path, 'r', encoding='utf-8') as file:  
        line = file.readline()  # 读取所有行，每行作为一个字符串 
        # 去除行尾的换行符，并分割字符串  
        fields = line.strip().split('|')  
    # 输出分割后的第一个字段name  
    return(fields[0])

def get_file_records(file_path):
    # 打开文件并读取内容
    
    with open(file_path, 'r', encoding='utf-8') as file:  
        line = file.readline()  # 读取所有行，每行作为一个字符串 
        # 去除行尾的换行符，并分割字符串  
        fields = line.strip().split('|')  
    # 输出分割后的第五个字段记录数  
    return(fields[4])


def write_to_txt(file_path,flg_path):  
    name=get_file_name(flg_path)
    file_size = get_file_size(file_path)  
    last_modified_time_day = get_last_time(file_path,'day')  
    last_modified_time_hms = get_last_time(file_path,'hms') 
    records= get_file_records(flg_path)
    md5_value = get_file_md5(file_path)   
    # 确保每个字段都占60个字符  
    name_formatted=name.ljust(60)
    file_size_formatted = file_size.ljust(16)   
    last_modified_formatted_day = last_modified_time_day.ljust(8) 
    last_modified_formatted_hms = last_modified_time_hms.ljust(6)
    records_formatted=records.ljust(12)
    md5_formatted = md5_value.ljust(64)
    emfield=" ".ljust(64) 
    #记录日志
    logging.info('文件名称是：======================================================  ')
    logging.info('文件名称是：  '+name_formatted)
    logging.info('文件大小是：  '+file_size_formatted)
    logging.info('文件日期是：  '+last_modified_formatted_day)
    logging.info('文件时间是：  '+last_modified_formatted_hms)
    logging.info('文件记录数:   '+records_formatted)
    logging.info('文件md5码:    '+md5_formatted)
    logging.info('文件名称是：======================================================  ')
    # 写入txt文件  
    with open(flg_path, "w",newline='') as txt_file:  
        txt_file.write(f"{name_formatted}|{file_size_formatted}|{last_modified_formatted_day}|{last_modified_formatted_hms}|{records_formatted}|{md5_formatted}|{emfield}\n")
# 使用函数  







def main():
    if len(sys.argv) > 1:
        dir = sys.argv[1]
        filename1=sys.argv[2]
        filename2=sys.argv[3]
    else:
        print("参数输入错误")
    
    file_path=get_file_path(dir,filename1)
    flg_path=get_file_path(dir,filename2)
    # 配置日志基本设置  
    logging.basicConfig(  
        filename=dir+'/databs.log',    # 日志文件名，如果没有这个参数，日志输出到console  
        filemode='a',              # 文件写入模式，“w”会覆盖之前的日志，“a”会追加到之前的日志  
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志格式  
        level=logging.DEBUG        # 设置日志级别，这里设置为DEBUG，会记录所有级别的日志 
          )  

    write_to_txt(file_path, flg_path) 


if __name__ == "__main__":
    main()



# file_path=get_file_path(dir,'zyhg_txt')
# print(file_path)
# dir=D:\data\postModify
# flg_path=get_file_path(dir,'zyhg_flg')
# file_path = 'C:/Users/yao/Desktop/zxbs3801820240411001.rar'  
# output_txt_path=get_file_path(dir,'zyhg_flg')
# write_to_txt(file_path, flg_path)
# print(get_file_md5(file_path))
# print(get_last_time(file_path,'day'))
# print(get_last_time(file_path,'hms'))
# print(get_file_size(file_path))
# print(get_file_name('C:/Users/yao/Desktop/zxbs3801820240411001.flg'))