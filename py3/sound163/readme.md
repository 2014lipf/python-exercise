# 爬网易云音乐评论并生成词云


# 使用

## 库
python3 + 第三方库
```
from selenium import webdriver
import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np
```

## 安装 chrome 和下载对应版本 chromedirver

http://npm.taobao.org/mirrors/chromedriver/

此版本为 78.0.3904.105 

## 配置 `config.json`
- `id` 网易云音乐id 
- `page` 爬取页数
- `useCache` 是否使用缓存
- `font_path` 字体路径
- `mask` maks图片路径
- `chromedriver` chromedriver路径

```
{
	"id":"1336789644",
	"page": 100,
	"useCache": true,
	"font_path": "./SimHei.ttf",
	"mask": "mask.png",
	"chromedriver": "chromedriver"
}
```

## 运行 `sound.py`