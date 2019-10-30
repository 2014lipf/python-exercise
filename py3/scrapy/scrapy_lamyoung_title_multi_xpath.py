
#author lamyoung

import requests
from multiprocessing.dummy import Pool
import lxml.html
import re

def scrapy(index):
	page_url = '';
	if index>1:
		page_url=f'page{index}/'
	url=f'http://lamyoung.com/{page_url}';
	print(url);
	html=requests.get(url);
	if html.status_code == 200:
		html_bytes=html.content;
		html_str=html_bytes.decode();
		selector = lxml.html.fromstring(html_str);
		all_items=selector.xpath('//div[@class="post-preview"]')
		write_content=''
		for item in all_items:
			links = item.xpath('a/@href') 
			title=item.xpath('a/h2[@class="post-title"]/text()')
			title_0=re.search(r"\s*(.*[^\s])\s*",title[0]).group(1)
			write_content=f'{write_content}{title_0}\nhttp://lamyoung.com{links[0]}\n\n'
		return write_content
	else:
		return ''

pool = Pool(3);
orign_num=[x for x in range(1,10)];
result = pool.map(scrapy,orign_num);
write_content = '';
for c in result:
	write_content+=c;

with open('lamyoung_title_multi_xpath_out.txt','w',encoding='utf-8') as f:
	f.write(write_content)
