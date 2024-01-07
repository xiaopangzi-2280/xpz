#开始安装模块
#pip install requests
import requests

url = "https://zy.xywlapi.cc/qqapi"
num = int(input("请输入QQ号："))
params = {
     "qq":num
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    # 处理返回的数据
    phonenumber = data["phone"]
    zt = data["status"]
    diqu = data["phonediqu"]
    qq = data["qq"]
    code = data["message"]
    print("请求结果："+code+"\n"+"QQ 号："+qq+"\n"+"手机号："+phonenumber+"\n"+"地区："+diqu+"\n"+"------灰灰网络安全------")
else:
    print("错误的请求")
    
