
#author lamyoung

import requests
import json
import csv
from multiprocessing.dummy import Pool

headers = {
	'Accept': 'application/json' 
}

def scrapy(index):
	url=f'https://forum.cocos.org/c/Creator/l/latest?page={index}';
	print(url);
	html=requests.get(url,headers=headers);
	if html.status_code == 200:
		html_bytes = html.content;
		html_str = html_bytes.decode();
		data = json.loads(html_str);
		# print(data)
		all_items=data['topic_list']['topics']
		write_content=[];
		for item in all_items:
			slug = item['slug'];
			item_id = item['id']
			link = f'https://forum.cocos.org/t/{slug}/{item_id}'
			title = item['title'];
			like_count = item['like_count'];
			like_count = item['like_count'];
			posts_count = item['posts_count'];
			views = item['views'];
			created_at = item['created_at'];
			write_content.append({'标题': title, '链接': link
				, '点赞':like_count , '回复':posts_count
				, '浏览':views , '发帖时间':created_at
				});
		return write_content

	else:
		return [];

pool = Pool(3);
orign_num=[x for x in range(0,10)];
result = pool.map(scrapy,orign_num);

with open('ccc_title_link.csv', 'w', newline='') as csvfile:
    fieldnames = ('标题', '链接', '点赞', '回复','浏览', '发帖时间')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for write_content in result:
    	for _content in write_content:
    		 writer.writerow(_content);
