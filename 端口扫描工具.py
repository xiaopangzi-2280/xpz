import requests

print("【欢迎使用 GitHub：xiaopangzi-2280】")

url = "https://v.api.aa1.cn/api/api-port/go.php"
params = {
    "ip": input("请输入网址或IP地址：")
}

response = requests.get(url, params=params)
data = response.text

print(data)