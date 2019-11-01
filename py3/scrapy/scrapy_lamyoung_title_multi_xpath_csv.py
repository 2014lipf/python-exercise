
#author lamyoung

import requests
from multiprocessing.dummy import Pool
import lxml.html
import csv

def scrapy(index):
	page_url = '';
	if index>1:
		page_url=f'page{index}/'
	url=f'http://lamyoung.com/{page_url}';
	print(url);
	html=requests.get(url);
	if html.status_code == 200:
		html_bytes=html.content;
		selector = lxml.html.fromstring(html_bytes);
		all_items=selector.xpath('//div[@class="post-preview"]')
		write_content=[];
		for item in all_items:
			links = item.xpath('a/@href') 
			title=item.xpath('a/h2[@class="post-title"]/text()')
			title_0=title[0].strip();
			write_content.append({'title': title_0, 'link': f'http://lamyoung.com{links[0]}'});
		return write_content
	else:
		return [];

pool = Pool(3);
orign_num=[x for x in range(1,10)];
result = pool.map(scrapy,orign_num);

with open('lamyoung_title_multi_xpath_out.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for write_content in result:
    	for _content in write_content:
    		 writer.writerow(_content);
