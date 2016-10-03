
import requests
from bs4 import BeautifulSoup
import re


def crawl_db(target):
    y = requests.get('http://data.bootex.xyz:28017/')
    soup = BeautifulSoup(y.text,'html.parser')
    prev_log_list = soup.findAll("pre")
    log_list = [re.sub("(<\/?pre>|\t)","",str(log)) for log in prev_log_list]

    if target == "status":
        return str(log_list[0])+str(log_list[1])

    if target == "log":
        return log_list[-1]


def crawl_hadoop_status():
    url = "http://data.bootex.xyz:8088/cluster"
    header = {'User-Agent': 'Mozilla/5.0'} # 헤더값 할당

    req = requests.Request('Get', url, headers=header) #헤더값과 파라미터값을 get방식으로 요청

    r = req.prepare()
    s = requests.Session()
    result = s.send(r)
    soup = BeautifulSoup(result.text,'html.parser')
    prev_table = soup.find("td",class_="content")
    print("Data",prev_table)
    return prev_table


def crawl_hadoop_info():
    url = "http://data.bootex.xyz:8088/cluster/cluster"
    header = {'User-Agent': 'Mozilla/5.0'}  # 헤더값 할당

    req = requests.Request('Get', url, headers=header)  # 헤더값과 파라미터값을 get방식으로 요청

    r = req.prepare()
    s = requests.Session()
    result = s.send(r)
    soup = BeautifulSoup(result.text, 'html.parser')
    prev_table = soup.find("div", class_="info-wrap")
    print(prev_table)
    return prev_table


class HADOOP_CRAWL:
    def get_status(self):
        pass
    def get_nodes(self):
        pass

if __name__ =="__main__":
    print (crawl_hadoop_status())
