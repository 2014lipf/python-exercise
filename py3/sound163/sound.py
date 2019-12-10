
# author lamyoung
import os
import json
from selenium import webdriver
import time
import random
import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np

CONFIG = {}
with open(f'config.json', 'r') as f:
	CONFIG = json.load(f)
print(CONFIG)

SOUND_ID = CONFIG['id']
PAGES = CONFIG['page']


comments_list = []
# 读取数据
filePath = f'./cache/{SOUND_ID}-{PAGES}.json'
if(CONFIG['useCache'] and os.path.isfile(filePath)):
	with open(filePath,'r') as f:
	    comments_list = json.load(f)
else:
	driver = webdriver.Chrome(CONFIG['chromedriver'])
	driver.get(f'https://music.163.com/#/song?id={SOUND_ID}')
	driver.switch_to.frame('g_iframe')

	comments_list = []
	for page in range(1,CONFIG['page']+1):
		print(f'page-->{page}')
		element_list = driver.find_elements_by_xpath('//div[@class="cnt f-brk"]')
		list_len = len(element_list)
		print(list_len)
		if(list_len<1):
			print('结束！')
			break
		for element in element_list:
			comments_list.append(element.text.split("：", 1)[-1])

		next_button = driver.find_element_by_xpath('//a[starts-with(@class,"zbtn znxt js-n-")]')
		driver.execute_script('arguments[0].click();', next_button)
		time.sleep(1+random.random()*2)
	# print(comments_list)
	with open(filePath,'w') as f:
		json.dump(comments_list,f, ensure_ascii=False, indent=4) 


# 词云处理
image_mask = np.array(Image.open(CONFIG['mask']))
# print(comments_list)
wordlist = jieba.cut(';'.join(comments_list))
# 词云处理
wordcloud = WordCloud(font_path=CONFIG['font_path'], background_color='white', mask=image_mask, scale=1.5).generate(' '.join(wordlist))
# 保存图
wordcloud.to_file(f'./result/{SOUND_ID}-{PAGES}.png')
