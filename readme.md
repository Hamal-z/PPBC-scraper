### PPBC中国植物图像库爬虫

最近在做一个课设需要大量花卉植物的图片来做训练集，于是写了一个爬虫，从中国植物图像库抓图。

--------

使用前需要在[中国植物图像库](http://www.plantphoto.cn)上找到所需植物的种（Species），例如:

> 被子植物门 Angiospermae >> 白花丹科 Plumbaginaceae >> 白花丹属 Plumbago >> 白花丹 Plumbago zeylanica

找到白花丹种的网址如下 http://www.plantphoto.cn/sp/26094

网址末端可找到sp号`26094`，这个便是白花丹的唯一标识。

-------
可获取多个sp号后一起爬取，具体设置在ppbc.py文件中可以找到。

scrapy自带缩略图功能，但不是等比例压缩，重写PicscrapyPipeline部分函数，在使用Pipeline爬图的同时用PIL等比例压缩，保存原图和压缩图，图片按编号顺序命名、按花卉名称分文件夹保存。

---------
Scrapy版本： `1.5.0`

Python版本：`3.6.4`


