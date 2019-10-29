
#author lamyoung

import requests
import re
from multiprocessing.dummy import Pool

regex = r"<a href=\"(.*)\">[\s]*?<h2 class=\"post-title\">[\s]*(.*)[\s]*</h2>[\s\S]*?</a>"

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
		# print(html_str)
		all_items=re.findall(regex,html_str);
		# print(all_items)
		write_content=''
		for item in all_items:
			write_content=f'{write_content}\n{item[1]}\nhttp://lamyoung.com{item[0]}\n'
		return write_content
	else:
		return ''

pool = Pool(3);
orign_num=[x for x in range(1,10)];

result = pool.map(scrapy,orign_num);
# print(f'result : {result}')

write_content = '';
for c in result:
	write_content+=c;

with open('lamyoung_title_multi_out.txt','w',encoding='utf-8') as f:
	f.write(write_content)
