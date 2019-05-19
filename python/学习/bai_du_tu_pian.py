import requests
import json
import os


class bai_du():
    tu_pian_url = []
    s = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3302.400 QQBrowser/9.6.11768.400',
    }

    def huo_qu(self, guan_jian_zi, ye_ma, zheng_zhang):
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=' + guan_jian_zi + \
              '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + guan_jian_zi + \
              '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=' + \
              str(ye_ma) + '&rn=30&gsm=5a&1503494207964='
        nei_rong = self.s.get(url, headers=self.headers)
        nei_rong.encoding = 'utf-8'
        try:
            nei_rong = json.loads(nei_rong.text)
            tu_pian = nei_rong['data']
            zong_gong = nei_rong['displayNum']
            ye_ma = ye_ma + zheng_zhang
            return self.chu_li(tu_pian, guan_jian_zi), ye_ma
        except Exception as e:
            print('第' + str(ye_ma) + '条到第' +
                  str((ye_ma + zheng_zhang)) + '条抓取失败')
            ye_ma = ye_ma + zheng_zhang
            return True, ye_ma

    def chu_li(self, data, guan_jian_zi):
        try:
            tiao = 0
            for zi in data:
                url = zi['thumbURL']
                wei_zi = zi['pageNum']
                wei_zi = '第' + str(wei_zi + 1) + '张'
                guan_jian_zi = guan_jian_zi
                tiao += 1
                if url[-3:] == 'jpg':
                    shu_ju = {'index': guan_jian_zi,
                              'url': url, 'location': wei_zi}
                    print(shu_ju)
                    self.bao_cun(guan_jian_zi, shu_ju)
        except Exception as e:
            if tiao == 0:
                print('完结')
            return tiao

    def bao_cun(self, guan_jian_zi, cur):
        if os.path.exists('D:/bai_du_tu_pian/' + guan_jian_zi):
            pass
        else:
            os.makedirs('D:/bai_du_tu_pian/' + guan_jian_zi)
        shu_ju = self.s.get(cur['url'], headers=self.headers).content
        with open(('D:/bai_du_tu_pian/' + cur['index']) + '/' + cur['location'] + '.jpg', 'wb') as f:
            f.write(shu_ju)
            f.close()


if __name__ == '__main__':
    guan_jian_zi = input('输入搜索的关键字:\n')
    ye_ma = 0
    zheng_zhang = 30
    spider = bai_du()
    b = 1
    # qing_qiu = spider.huo_qu(guan_jian_zi, ye_ma, zheng_zhang)
    while b != 0:
        a = spider.huo_qu(guan_jian_zi, ye_ma, zheng_zhang)
        b = a[0]
        ye_ma = a[1] + zheng_zhang
