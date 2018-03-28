import scrapy
from ppbc.items import PicscrapyItem


class BaiduSpider(scrapy.Spider):
    name = 'ppbc'
    start_urls = ['http://www.plantphoto.cn']
    # 设置sp号
    flower = {
        '向日葵': 32129,
        '水仙': 41183,
        '虞美人': 15906,
        '康乃馨': 12880,
        '茶花': 15429,
        '迎春花': 26490,
    }
    pageNum = 15  # 设置要爬取的页数，一页20张图片

    def parse(self, response):
        i = 0
        for k, y in self.flower.items():
            for page in range(1, self.pageNum + 1):
                url = 'http://www.plantphoto.cn/ashx/getphotopage.ashx?page={page}&n=2&group=sp&cid={cid}'
                url = url.format(page=page, cid=y)
                yield scrapy.Request(url, meta={'flower': k, 'page': page, 'i': i}, callback=self.down)
            i += 1

    def down(self, response):
        page = response.meta['page']
        pre = response.meta['i']
        pids = response.css('div.img')
        for i in range(len(pids)):
            item = PicscrapyItem()
            pid = pids[i].css('div.img::attr(pid)').extract_first()
            item['title'] = (page - 1) * 20 + i + pre * self.pageNum * 20
            item['floweregory_name'] = response.meta['flower']
            img_path = 'http://img.plantphoto.cn/image2/l/' + pid + '.jpg'
            item['image_urls'] = [img_path]
            yield item
