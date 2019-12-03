# 用途
分析基金

# 环境
python3 + 第三方库
```
import requests
import pandas
import numpy
import matplotlib
import lxml
```

# 配置 `config.json`
`code` 配置基金代码, `useCache`是否使用缓存
```json
{
	"code":[
		"002736",
  		"003328",
  		"003547",
  		"000286",
  		"003847",
  		"161716",
  		"003327",
  		"160618",
  		"206018",
  		"000186"
	],
	"useCache":true
}

```

# 使用
运行 `fund_analysis.py`
