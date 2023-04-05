# -*- coding: utf-8 -*-
import lxml, sys
import requests
import time, datetime
from bs4 import BeautifulSoup
url5600='https://whattomine.com/coins?aq_5700=7&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5600xt=22&a_5600xt=true&aq_vega64=0&aq_vega56=0&aq_4090=0&aq_4080=0&aq_47Ti=0&aq_39Ti=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_37Ti=0&aq_3070=0&aq_3060Ti=0&aq_3060=0&aq_66=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_a5=0&aq_a45=0&aq_a4=0&aq_a2=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=8&aq_1070Ti=0&aq_1070=4&aq_10606=8&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=891.00&factor%5Beth_p%5D=2420.00&e4g=true&factor%5Be4g_hr%5D=891.00&factor%5Be4g_p%5D=2420.00&zh=true&factor%5Bzh_hr%5D=836.00&factor%5Bzh_p%5D=2420.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=27500.00&factor%5Bcng_p%5D=2420.00&factor%5Bs5r_hr%5D=0.00&factor%5Bs5r_p%5D=0.00&factor%5Bcx_hr%5D=0.00&factor%5Bcx_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=70.40&factor%5Bcc_p%5D=1760.00&cr29=true&factor%5Bcr29_hr%5D=68.20&factor%5Bcr29_p%5D=1760.00&factor%5Bhh_hr%5D=5500.00&factor%5Bhh_p%5D=2420.00&ct32=true&factor%5Bct32_hr%5D=3.74&factor%5Bct32_p%5D=2420.00&eqb=true&factor%5Beqb_hr%5D=451.00&factor%5Beqb_p%5D=2420.00&factor%5Bb3_hr%5D=0.00&factor%5Bb3_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&factor%5Bal_hr%5D=1760.00&factor%5Bal_p%5D=2200.00&factor%5Bops_hr%5D=253.00&factor%5Bops_p%5D=1980.00&eqz=true&factor%5Beqz_hr%5D=532.40&factor%5Beqz_p%5D=2420.00&zlh=true&factor%5Bzlh_hr%5D=521.40&factor%5Bzlh_p%5D=2420.00&kpw=true&factor%5Bkpw_hr%5D=385.00&factor%5Bkpw_p%5D=2860.00&ppw=true&factor%5Bppw_hr%5D=0.00&factor%5Bppw_p%5D=0.00&factor%5Bnx_hr%5D=506.00&factor%5Bnx_p%5D=2200.00&factor%5Bfpw_hr%5D=396.00&factor%5Bfpw_p%5D=2860.00&factor%5Bvh_hr%5D=13.64&factor%5Bvh_p%5D=2420.00&factor%5Bcost%5D=0.0&factor%5Bcost_currency%5D=USD&sort=Profit24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate'
url5700='https://whattomine.com/coins?aq_5600xt=22&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=7&a_5700=true&aq_vega64=0&aq_vega56=0&aq_4090=0&aq_4080=0&aq_47Ti=0&aq_39Ti=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_37Ti=0&aq_3070=0&aq_3060Ti=0&aq_3060=0&aq_66=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_a5=0&aq_a45=0&aq_a4=0&aq_a2=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=8&aq_1070Ti=0&aq_1070=4&aq_10606=8&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=385.00&factor%5Beth_p%5D=910.00&e4g=true&factor%5Be4g_hr%5D=385.00&factor%5Be4g_p%5D=910.00&zh=true&factor%5Bzh_hr%5D=322.00&factor%5Bzh_p%5D=980.00&cnh=true&factor%5Bcnh_hr%5D=9450.00&factor%5Bcnh_p%5D=770.00&cng=true&factor%5Bcng_hr%5D=10500.00&factor%5Bcng_p%5D=980.00&factor%5Bs5r_hr%5D=0.00&factor%5Bs5r_p%5D=0.00&factor%5Bcx_hr%5D=9.80&factor%5Bcx_p%5D=840.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=26.60&factor%5Bcc_p%5D=630.00&cr29=true&factor%5Bcr29_hr%5D=25.90&factor%5Bcr29_p%5D=630.00&factor%5Bhh_hr%5D=1750.00&factor%5Bhh_p%5D=770.00&ct32=true&factor%5Bct32_hr%5D=2.45&factor%5Bct32_p%5D=910.00&eqb=true&factor%5Beqb_hr%5D=168.00&factor%5Beqb_p%5D=980.00&factor%5Bb3_hr%5D=0.00&factor%5Bb3_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&factor%5Bal_hr%5D=700.00&factor%5Bal_p%5D=910.00&factor%5Bops_hr%5D=95.20&factor%5Bops_p%5D=770.00&eqz=true&factor%5Beqz_hr%5D=210.00&factor%5Beqz_p%5D=980.00&zlh=true&factor%5Bzlh_hr%5D=238.00&factor%5Bzlh_p%5D=980.00&kpw=true&factor%5Bkpw_hr%5D=161.00&factor%5Bkpw_p%5D=1120.00&ppw=true&factor%5Bppw_hr%5D=84.00&factor%5Bppw_p%5D=1050.00&factor%5Bnx_hr%5D=175.00&factor%5Bnx_p%5D=840.00&factor%5Bfpw_hr%5D=150.50&factor%5Bfpw_p%5D=1120.00&factor%5Bvh_hr%5D=5.74&factor%5Bvh_p%5D=910.00&factor%5Bcost%5D=0.0&factor%5Bcost_currency%5D=USD&sort=Profit24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate'
url1080='https://whattomine.com/coins?aq_5700=7&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5600xt=22&aq_vega64=0&aq_vega56=0&aq_4090=0&aq_4080=0&aq_47Ti=0&aq_39Ti=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_37Ti=0&aq_3070=0&aq_3060Ti=0&aq_3060=0&aq_66=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_a5=0&aq_a45=0&aq_a4=0&aq_a2=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=8&a_1080=true&aq_1070Ti=0&aq_1070=4&aq_10606=8&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=268.00&factor%5Beth_p%5D=1360.00&e4g=true&factor%5Be4g_hr%5D=272.00&factor%5Be4g_p%5D=1360.00&zh=true&factor%5Bzh_hr%5D=536.00&factor%5Bzh_p%5D=1280.00&cnh=true&factor%5Bcnh_hr%5D=5840.00&factor%5Bcnh_p%5D=880.00&cng=true&factor%5Bcng_hr%5D=14400.00&factor%5Bcng_p%5D=1280.00&factor%5Bs5r_hr%5D=3.44&factor%5Bs5r_p%5D=800.00&factor%5Bcx_hr%5D=0.00&factor%5Bcx_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=1920.00&factor%5Beqa_p%5D=1200.00&cc=true&factor%5Bcc_hr%5D=48.80&factor%5Bcc_p%5D=1280.00&cr29=true&factor%5Bcr29_hr%5D=52.00&factor%5Bcr29_p%5D=1280.00&factor%5Bhh_hr%5D=2800.00&factor%5Bhh_p%5D=880.00&ct32=true&factor%5Bct32_hr%5D=2.32&factor%5Bct32_p%5D=1200.00&eqb=true&factor%5Beqb_hr%5D=160.00&factor%5Beqb_p%5D=1200.00&factor%5Bb3_hr%5D=0.00&factor%5Bb3_p%5D=0.00&ns=true&factor%5Bns_hr%5D=12000.00&factor%5Bns_p%5D=1200.00&factor%5Bal_hr%5D=476.00&factor%5Bal_p%5D=1280.00&factor%5Bops_hr%5D=84.00&factor%5Bops_p%5D=1360.00&eqz=true&factor%5Beqz_hr%5D=306.40&factor%5Beqz_p%5D=1200.00&zlh=true&factor%5Bzlh_hr%5D=352.00&factor%5Bzlh_p%5D=1360.00&kpw=true&factor%5Bkpw_hr%5D=135.20&factor%5Bkpw_p%5D=1280.00&ppw=true&factor%5Bppw_hr%5D=135.20&factor%5Bppw_p%5D=1280.00&factor%5Bnx_hr%5D=88.00&factor%5Bnx_p%5D=1040.00&factor%5Bfpw_hr%5D=132.00&factor%5Bfpw_p%5D=1280.00&factor%5Bvh_hr%5D=4.16&factor%5Bvh_p%5D=1200.00&factor%5Bcost%5D=0.0&factor%5Bcost_currency%5D=USD&sort=Profit24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate'
url=[url1080,url5600,url5700]
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition Yx 03)'}
def whattomine():
    coins = 5# количество монет для вывода с самой высокой доходностью
    try:
        for ur in url:
            responce = requests.get(ur, headers=headers)
            if responce.status_code<300:
                res=responce.text
                soup = BeautifulSoup(res, "lxml")
                tbody_tag = soup.tbody
                tbody = tbody_tag.find_all('div', class_='ms-5 d-flex justify-content-between')
                with open('log.txt', 'a') as log:
                    data = str(datetime.datetime.now())
                    log.write(data+ ' WtOM '+ 'status code ='+ str(responce.status_code)+'\n')

                list_dict_coin_incom=[]
                for tb in tbody: # Идем по  строкам
                    i = 0 #№ строки
                    if tb.find('a'): #выбираем нужные строки
                        tb_a=tb.find('a') # нашли нужный тег с названием
                        coin_name=tb.find('a').get_text() # забрали название
                        tr_class=tb_a.find_parent('tr').find_all('td') # пришли в <tr class> нужной строки
                        for strong in tr_class:
                            i+=1
                            if i==8: # нашли нужную строку для парсинга
                                incom=strong.find('strong').get_text() # доходность
                                dict_coin_incom={coin_name.strip():incom.strip()}# монета + доходность словарь
                                list_dict_coin_incom.append(str(ur)+ ' '+str(dict_coin_incom))# список монет с доходностью
                                #print (str(list_dict_coin_incom))

                quantity=0
                list_coin_incom=[]
                for coin in list_dict_coin_incom:
                    quantity+=1
                    list_coin_incom.append(coin)
                    print(coin)
                    yield coin
                    if quantity == coins:
                        break
    except:
        print(sys.exc_info())
        return 'error'#, sys.exc_info()

if __name__ == '__main__':
    whattomine()