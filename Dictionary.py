'''
This program is to get German verbs from an German dictionary.
Implemented:
    Enter a verb and get its different forms from www.godic.net and de.wiktionary.org
'''
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

#德语助手词性、意思、例句
def get_godic(word):
    url = "http://www.godic.net/dicts/de/" + word
    resp = requests.get(url,headers=headers)
    text = resp.content.decode('utf-8')
    # print(text)
    html = etree.HTML(text)

    # 选取当前节点的所有后代元素（子、孙等）以及当前节点本身 的内容
    divs = html.xpath('//div[@id="ExpFCChild"]/descendant-or-self::text()')

    if divs[0] == "赞" and divs[1] == "踩":
        divs = divs[6:]
    for div in divs:
        print(div)

    # spans = html.xpath('//div[@id="ExpFCChild"]/span[@class="cara"]|//div[@id="ExpFCChild"]/span[@class="exp"]|//div[@id="ExpFCChild"]/span[@class="eg"]|//div[@id="ExpFCChild"]/span[@class="eg"]/i|//div[@id="ExpFCChild"]')
    # for span in spans:
    #     if span.xpath('./text()') != []:
    #         print(span.xpath('./text()')[0])

#Wiki变位
def get_Wiki(word):
    url = "https://de.wiktionary.org/wiki/" + word
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    # print(text)
    html = etree.HTML(text)
    #获取单词变位
    tbodys = html.xpath('//tbody')
    for tbody in tbodys:
        if len(tbody.xpath('./tr')) == 11:
            ts = tbody.xpath('./tr')
            print("Präsens ich: "+str(ts[1].xpath('./td/a/text()')))#现在时
            print("Präsens du: "+str(ts[2].xpath('./td/a/text()')))#现在时
            print("Präsens er/sie/es: "+str(ts[3].xpath('./td/a/text()')))#现在时
            print("Präteritum ich: "+str(ts[4].xpath('./td/a/text()')))#过去时
            print("KonjunktivII ich: "+str(ts[5].xpath('./td/a/text()')))#第二虚拟式
            print("PartizipII: "+str(ts[9].xpath('./td/a/text()')))#完成时

def main():
    print("请输入德语单词：")
    word = input()
    print("###Wiki变位###")
    get_Wiki(word)
    print("###德语助手###")
    get_godic(word)


if __name__ == '__main__':
    main()