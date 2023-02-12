'''
This code is used to get the vehicle information on the used car website.
'''
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Cookie': 'uuid=6aaa1b99-b0c7-4a71-c167-8cbc3da5a094; ganji_uuid=1185666894244847088597; antipas=9U2112312229O99Yne1164h997; clueSourceCode=%2A%2300; user_city_id=-1; sessionid=5d73b4b5-e46a-45ef-a1ef-6f4eb3c13d44; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_google%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%226aaa1b99-b0c7-4a71-c167-8cbc3da5a094%22%2C%22ca_city%22%3A%22bj%22%2C%22sessionid%22%3A%225d73b4b5-e46a-45ef-a1ef-6f4eb3c13d44%22%7D; close_finance_popup=2020-03-26; cityDomain=www; preTime=%7B%22last%22%3A1585230193%2C%22this%22%3A1583581262%2C%22pre%22%3A1583581262%7D; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1585229750,1585230195; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1585230195'
}#数据头

#获取详情页面的地址
def get_detail_urls(url):
    # 访问索引页
    resp = requests.get(url, headers=headers)
    # 获取详情页面url
    text = resp.content.decode('utf-8')
    # print(text)

    html = etree.HTML(text)

    ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    # print(ul)

    ls = ul.xpath('./li')
    # print(ls)
    detail_urls = []
    for i in ls:
        detail_url = i.xpath('./a/@href')
        # './a/@href'查找具体内容；'./a[@href]'查找有href标签的a标签（费具体内容）
        detail_url = 'https://www.guazi.com' + detail_url[0]
        detail_urls.append(detail_url)
        # print(detail_url)
    return detail_urls

#解析单个详情页面内容
def parse_detail_page(detail_url):
    detail_resp = requests.get(detail_url, headers=headers)
    detail_text = text = detail_resp.content.decode('utf-8')
    detail_html = etree.HTML(detail_text)
    title = detail_html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
    title = title.replace(r'\r\n','').strip()#replace替换换行符为空白，strip去除首尾空格
    # print(title)
    info = detail_html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')#获取li标签下所有span标签的内容
    # print(info)
    infos = {}  # 字典储存每辆车的数据
    infos['title'] = title
    infos['time'] = info[0]
    infos['km'] = info[1]
    infos['replacement'] = info[2]
    infos['speedbox'] = info[3]
    print(infos)
    return infos

#保存数据
def save_data(infos,f):
    f.write('{},{},{},{},{}\n'.format(infos['title'],infos['time'],infos['km'],infos['replacement'],infos['speedbox']))

def main():

    # 获取第一页内容
    base_url = 'https://www.guazi.com/www/benz/o{}c-1/'

    with open('guazi_cs.txt', 'a', encoding='utf-8') as f:
        for x in range(1,4):#1到3页
            url = base_url.format(x)
            detail_urls = get_detail_urls(url)#获取详情页面的地址
            for detail_url in detail_urls[:5]:#前5辆车
                infos = parse_detail_page(detail_url)#解析单个详情页面内容
                save_data(infos,f)#保存数据

if __name__  == '__main__' :
    main()
