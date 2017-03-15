# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pymongo
import time

client=pymongo.MongoClient('localhost',27017)
weatherTTL=client['weatherTTL']
sheet_weather_1=weatherTTL['sheet_weather_1']
sheet_weather_2=weatherTTL['sheet_weather_2']


url_list_all=[""]
url_list_13attr=[""]
url_list_12attr=[""]
url_list_12attr_match=[""]







for i in range(0,12):
    for j in range(0,day[i]):

        url = root1_url + str(month[i]) + "/" + str((j+1)) + root2_url

        wb_data = requests.get(url)
        print(url)
        url_list_all.append(url)
        soup = BeautifulSoup(wb_data.text, "lxml")

        # time=soup.select('#obsTable > tbody > tr:nth-of-type(1) > td:nth-of-type(1)')
        shijians = soup.select('#obsTable > tbody > tr > td:nth-of-type(1)')
        qiwens = soup.select('#obsTable > tbody > tr > td:nth-of-type(2)')
        fenglengwens = soup.select('#obsTable > tbody > tr > td:nth-of-type(3)')
        ludians = soup.select('#obsTable > tbody > tr > td:nth-of-type(4)')
        shidus = soup.select('#obsTable > tbody > tr > td:nth-of-type(5)')
        qiyas = soup.select('#obsTable > tbody > tr > td:nth-of-type(6)')
        nengjiandus = soup.select('#obsTable > tbody > tr > td:nth-of-type(7)')
        winddirs = soup.select('#obsTable > tbody > tr > td:nth-of-type(8)')
        fengsus = soup.select('#obsTable > tbody > tr > td:nth-of-type(9)')
        shunjianfengsus = soup.select('#obsTable > tbody > tr > td:nth-of-type(10)')
        precips = soup.select('#obsTable > tbody > tr > td:nth-of-type(11)')
        huodongs = soup.select('#obsTable > tbody > tr > td:nth-of-type(12)')
        zhuangkuangs = soup.select('#obsTable > tbody > tr > td:nth-of-type(13)')

        for shijian, qiwen, fenglengwen, ludian, shidu, qiya, nengjiandu, winddir, fengsu, shunjianfengsu, precip, huodong, zhuangkuang in zip(
                shijians, qiwens, fenglengwens, ludians, shidus, qiyas, nengjiandus, winddirs, fengsus, shunjianfengsus,
                precips, huodongs, zhuangkuangs):
            shijian_c = shijian.get_text()
            # _c means _content
            qiwen_c = qiwen.get_text()
            fenglengwen_c = fenglengwen.get_text()
            ludian_c = ludian.get_text()
            shidu_c = shidu.get_text()
            qiya_c = qiya.get_text()
            nengjiandu_c = nengjiandu.get_text()
            winddir_c = winddir.get_text()
            fengsu_c = fengsu.get_text()
            shunjianfengsu_c = shunjianfengsu.get_text()
            precip_c = precip.get_text()
            huodong_c = huodong.get_text()
            zhuangkuang_c = zhuangkuang.get_text()

            data = {
                "url": url,
                "month": month[i],
                "day": (j+1),
                'shijian': shijian_c,
                'qiwen':qiwen_c,
                'fenglengwen': fenglengwen_c,
                'ludian': ludian_c,
                'shidu': shidu_c,
                'qiya': qiya_c,
                'nengjiandu': nengjiandu_c,
                'winddir': winddir_c,
                'fengsu': fengsu_c,
                'shunjianfengsu': shunjianfengsu_c,
                'precip': precip_c,
                'huodong': huodong_c,
                'zhuangkuang': zhuangkuang_c
            }

            sheet_weather_1.insert_one(data)
            print(url)
            url_list_13attr.append(url)



aa=set(url_list_all)
bb=set(url_list_13attr)
url_list_12attr=list(aa.difference(bb))



for i in range(len(url_list_12attr)):
    # print(url_list_12attr[i])
    # print("-")
    url=url_list_12attr[i]

    wb_data = requests.get(url)

    soup = BeautifulSoup(wb_data.text, "lxml")

    # time=soup.select('#obsTable > tbody > tr:nth-of-type(1) > td:nth-of-type(1)')
    shijians = soup.select('#obsTable > tbody > tr > td:nth-of-type(1)')
    qiwens = soup.select('#obsTable > tbody > tr > td:nth-of-type(2)')

    ludians = soup.select('#obsTable > tbody > tr > td:nth-of-type(3)')
    shidus = soup.select('#obsTable > tbody > tr > td:nth-of-type(4)')
    qiyas = soup.select('#obsTable > tbody > tr > td:nth-of-type(5)')
    nengjiandus = soup.select('#obsTable > tbody > tr > td:nth-of-type(6)')
    winddirs = soup.select('#obsTable > tbody > tr > td:nth-of-type(7)')
    fengsus = soup.select('#obsTable > tbody > tr > td:nth-of-type(8)')
    shunjianfengsus = soup.select('#obsTable > tbody > tr > td:nth-of-type(9)')
    precips = soup.select('#obsTable > tbody > tr > td:nth-of-type(10)')
    huodongs = soup.select('#obsTable > tbody > tr > td:nth-of-type(11)')
    zhuangkuangs = soup.select('#obsTable > tbody > tr > td:nth-of-type(12)')

    for shijian, qiwen, ludian, shidu, qiya, nengjiandu, winddir, fengsu, shunjianfengsu, precip, huodong, zhuangkuang in zip(
            shijians, qiwens,  ludians, shidus, qiyas, nengjiandus, winddirs, fengsus, shunjianfengsus,
            precips, huodongs, zhuangkuangs):
        shijian_c = shijian.get_text()
        # _c means _content
        qiwen_c = qiwen.get_text()

        ludian_c = ludian.get_text()
        shidu_c = shidu.get_text()
        qiya_c = qiya.get_text()
        nengjiandu_c = nengjiandu.get_text()
        winddir_c = winddir.get_text()
        fengsu_c = fengsu.get_text()
        shunjianfengsu_c = shunjianfengsu.get_text()
        precip_c = precip.get_text()
        huodong_c = huodong.get_text()
        zhuangkuang_c = zhuangkuang.get_text()

        data = {
            "url": url,
            'shijian': shijian_c,
            'qiwen':qiwen_c,
            'ludian': ludian_c,
            'shidu': shidu_c,
            'qiya': qiya_c,
            'nengjiandu': nengjiandu_c,
            'winddir': winddir_c,
            'fengsu': fengsu_c,
            'shunjianfengsu': shunjianfengsu_c,
            'precip': precip_c,
            'huodong': huodong_c,
            'zhuangkuang': zhuangkuang_c
        }
        sheet_weather_2.insert_one(data)
        print(url)
        url_list_12attr_match.append(url)

print("---------------------")
cc=set(url_list_12attr_match)
dd=set(url_list_12attr)
unmatch=list(cc.difference(dd))
print(unmatch)
