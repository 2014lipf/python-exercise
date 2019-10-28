
#author:lamyoung

import requests
import re

write_content = ''
regex = r"<a href=\"(.*)\">[\s]*?<h2 class=\"post-title\">[\s]*(.*)[\s]*</h2>[\s\S]*?</a>"

index=1
while True:
	page_url = '';
	if index>1:
		page_url=f'page{index}/'
	url=f'http://lamyoung.com/{page_url}';
	print(url);
	html=requests.get(url);
	if html.status_code != 200:
		print(html);
		break;
		pass
	html_bytes=html.content;
	html_str=html_bytes.decode();
	# print(html_str)
	all_items =re.findall(regex,html_str);
	# print(all_items)
	for item in all_items:
		write_content =f'{write_content}\n{item[1]}\nhttp://lamyoung.com{item[0]}\n'
		pass

	index+=1;
	
with open('lamyoung_title_out.txt','w',encoding='utf-8') as f:
	f.write(write_content)
