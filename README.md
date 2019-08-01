# simple-crawler
环境： Python3

依赖包： scrapy，通过pip安装即可

功能： 爬取Stackoverflow上votes数最多的JavaScript语言的前30万条问题的标题，以及问题详情页面的url、赞数最高的答案中的第一个代码段、赞数最高答案的赞数。如要获得其它语言的信息，比如Python，则可在`spiders/sto.py`中的第10行将`start_urls`变量中的`javascript`字段换成`python`即可。

运行方式： 在项目目录下执行 `scrapy crawl sto -o js_data.json`，-o后面的参数代表输出文件。

注： 在`settings.py`中可以设置并发请求数量、发送请求的延迟、请求头的User_Agent等。经测试可知Stackoverflow网站对于爬虫爬取速度的检测阈值差不多在0.7秒左右，再低则会触发保护机制，因而目前的设置中是每0.7秒发送一次请求，即获取到一个问题的信息需要0.7秒，爬取30万数据大约需要0.7*300000=210000秒，即大约58小时。