import yaml
import os,sys
sys.path.append(os.getcwd())
sys.path.append('..') #表示导入当前文件的上层目录到搜索路径中
sys.path.append('/oa/data') # 绝对路径
sys.path.insert(1, "./data")
#file_name="./data/login_data.yaml"
#解析login_yml文件内容
def yaml_file(file_name,key):
    with open(file_name,'r',encoding='utf-8') as f:
        data = yaml.load(f)[key]
        case_data_list = list()
        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list

