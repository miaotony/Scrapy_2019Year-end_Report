"""
2019 Year-end report
爬取QQ小程序 【年终报告单/2019年终总结】中的图片
@time: 20191204
@Author: miaotony

"""

import requests
import os

os.makedirs('./img/', exist_ok=True)
URL = 'https://oos-pic.oss-cn-beijing.aliyuncs.com/2019%E5%B9%B4%E7%BB%88%E6%80%BB%E7%BB%93/'
"""下载图片"""
for i in range(1, 20):
    img_name = str(i) + '.png'
    img_url = URL + img_name
    try:
        r = requests.get(img_url, stream=True)
        # print(r.text)
        if 'Error' not in r.text:
            with open('./img/%s' % img_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
            print('Saved %s successfully.' % img_name)
        else:
            print('Error')
    except Exception as e:
        print(e)
