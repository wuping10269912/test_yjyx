import os,sys
sys.path.append(os.getcwd())
sys.path.append('..') #表示导入当前文件的上层目录到搜索路径中
sys.path.append('/oa/base') # 绝对路径
sys.path.insert(1, "./base")
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class AdduserPage(BaseAction):
    adduser=By.XPATH,"//*[contains(@text,'客户新增')]"
    usernameadd=By.XPATH,"//*[contains(@index,'0')]"
    iphoneadd=By.ID,"aac030"
    qqadd=By.ID,"aac01u"
    user_type=By.XPATH,"//*[contains(@text,'腾讯课堂(私信)')]"
    user_status=By.XPATH,"//*[constain(@text,'意向客户')]"
    save_button=By.ID,"TitleButton"
    def click_adduser(self):
        self.click(self.adduser)
    def click_addusername(self):
        self.click(self.usernameadd)
    def input_addusername(self,text):
        self.send_keys(self.usernameadd,text)
    def input_iphone(self,text1):
        self.send_keys(self.iphoneadd,text1)
    def input_qq(self,text2):
        self.send_keys(self.qqadd,text2)
    def select_usertype(self):
        self.click(self.user_type)
    def select_userstatus(self):
        self.click(self.user_status)
    def click_save(self):
        self.click(self.save_button)