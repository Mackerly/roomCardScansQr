import requests
import time
import os

roomcode='22158be7-e22c-462e-a0b2-fa4c78e4af83'

Token = os.environ["TOKEN"]
print(Token)

headers = {
    'Host': 'jkksh.hnhfpc.gov.cn',
    'Origin': 'https://jkkgzh.hnhfpc.gov.cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'token={}'.format(Token),
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b37) NetType/4G Language/zh_CN',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Referer': 'https://jkkgzh.hnhfpc.gov.cn/',
    'token': Token,
}

def scanroomcard(roomcode,no=0):
    url = 'https://jkksh.hnhfpc.gov.cn/csm/jkxbservice.ashx?action=newaddroomcardv1&roomcode={roomcode}'.format(roomcode=roomcode)
    r = requests.get(url,headers=headers)
    if (r.status_code == 200) and r.json()["errno"] == 0 and '发送成功' in r.json()["message"]:
        print('正在扫场所码：{} {} ===> {} {}'.format(str(no + 1),r.json()['data']['companyName'],r.json()['data']['oneCompanyName'],r.json()['data']['addressName']))
    else:
        print(r.text)

def getroomcodes():
    roomcodes = open('roomcode.txt','r',encoding='utf-8').readlines()
    return roomcodes

if __name__ == "__main__":
    start =time.time()
    rmcs = getroomcodes()
    times = 2 # 重复 times 次
    for xx in range(times): 
        print('正在开始第 {} 轮扫码'.format(str(xx+1)))
        for x in range(len(rmcs)):
            roomcode = rmcs[x].replace('\n','')
            scanroomcard(roomcode,x)
            time.sleep(5) # 休息5秒钟。
    end = time.time()
    msg = '完成 {} 轮场所码扫码，共耗时 {} 分钟'.format(str(times),str((end-start)/60))
    print(msg)
