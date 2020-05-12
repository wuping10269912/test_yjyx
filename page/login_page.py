from selenium.webdriver.common.by import By
from base.base_action import *
import os,sys
sys.path.append(os.getcwd())
sys.path.append('..') #表示导入当前文件的上层目录到搜索路径中
sys.path.append('/oa/base') # 绝对路径
sys.path.insert(1, "./base")

class LoginPage(BaseAction):
    #准备元素
    app_click=By.CLASS_NAME,'android.widget.TextView'
    user_text=By.ID, 'edu.yjyx.student:id/et_name'
    pass_text=By.ID, 'edu.yjyx.student:id/et_password'
    login_button=By.ID, 'edu.yjyx.student:id/bt_submit'
    my_button=By.XPATH,"//*[contains(@text,'我的')]"
    setting_button=By.ID,"edu.yjyx.student:id/setting"
    name_xiugai=By.ID,"edu.yjyx.student:id/rl_name"
    name_text=By.XPATH,"//*[contains(@text,'输入姓名')]"
    sure_button=By.XPATH,"//*[contains(@text,'确定')]"
    # def click_app(self):
    #     self.click(self.app_click)
    def input_username(self,Text):
        self.send_keys(self.user_text,Text)
    def input_password(self,text):
        self.send_keys(self.pass_text,text)
    def click_login(self):
        self.click(self.login_button)
    def click_my(self):
        self.click(self.my_button)
    def click_setting(self):
        self.click(self.setting_button)
    def click_name(self):
        self.click(self.name_xiugai)
    def input_name(self,text1):
        self.send_keys(self.name_text,text1)
    def click_sure(self):
        self.click(self.sure_button)
