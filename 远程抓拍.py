#导入请求模块
import requests
import webbrowser

#经典开场白
print("【欢迎使用 GitHub：xiaopangzi-2280】"+"\n")

#💩山
API = "https://uso.link/?"
ckAPI = "http://uso.link/ck.php?id="

off = input("您要使用还是查询？【使用/查询】：")
if off == "查询":
    cxid = input("请输入ID进行查询：")
    idcx = (ckAPI+cxid)
    webbrowser.open(idcx, new=0, autoraise=True)
    print("---本轮脚本已结束---")
    
    
id = input("请输入一个ID：")
url = input("请输入点击后跳转的链接【默认链接请直接按回车】:")

params = {
    "id":id,
    "url1":url
}

if url == "":
    mr = (API+"id="+id+"&url="+"https://im.q.com"+"\n")
    print(mr)
else:
    diy = (API+"id="+id+"&url="+url+"\n")
    print(diy)
    
