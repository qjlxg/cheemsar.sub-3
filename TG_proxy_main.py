# w1770946466 北慕白  https://github.com/w1770946466/Auto_proxy
# aggregator
# coding=utf-8
import base64
import requests
import re
import time
import os
import threading
from tqdm import tqdm
import random, string
import datetime
from time import sleep
import chardet

#试用机场链接
home_urls =(
'http://api.xn--14ra41gd24b.xyz',
'http://api-0609.m55u97uleod7lm5.download',
'http://ciallo.elegy.icu:7001',
'http://cloudupup.com',
'http://dashabi.ping-zi-yun.icu',
'http://dingyue.myzone.site',
'http://dingyue2.qyjc.xyz',
'http://dingyue3.qyjc.xyz',
'http://dishujichang.xyz',
'http://dy.changyouVPN.top',
'http://dy.changyouvpn.top',
'http://dy.hpyjc.top',
'http://dy.xyyjc.top',
'http://em7.buzz',
'http://fanqiang88.top',
'http://fbapiv1.fbsublink.com',
'http://fdgdr0dg3.xbvpn.vip',
'http://filusdt.461553.best:1588',
'http://free.ninecloud.co',
'http://fs123121.cdn.22.jiacdnd123456789.com',
'http://g3i.buzz',
'http://gbtgurl01.org',
'http://ggiuwegivhe123.a123.bond',
'http://hpyjc.top',
'http://jjz.31465.cfd',
'http://jshou.top',
'http://laobideng.xyz',
'http://lianjiasub.work',
'http://ly.ccwink.cc',
'http://mf.kejifan88.top',
'http://mine.subcsyun.online',
'http://msvpn.gougouvpn.xyz:88',
'http://nangang.pro',
'http://s.33y.run',
'http://s.kalaa.me',
'http://s1.subcsyun.online',
'http://s3.subcsyun.online',
'http://s4.subcsyun.online',
'http://user.tsunaminet.cc',
'http://v2-1.806cms.top',
'http://vip.365cloud.me',
'http://vpn.gougouvpn.xyz:88',
'http://vps.huanshi88.sbs',
'http://www.fanqiang88.top',
'http://www.freeflyingcloud.xyz',
'http://www.mmsbs.buzz',
'http://www.pingzicloud.top',
'http://x1yjc.top',
'http://xbvpn.vip',
'http://xsj520.top',
'http://xyyjc.top',
'http://yy-cmi.mozhiti.top',
'http://yzxxy.top',
'https://12123.org',
'https://123abc.love',
'https://17852.xyz',
'https://196284.nginxzfd.xyz',
'https://1g.gay',
'https://1st.sub-airport.com',
'https://1ytcom01.1yunti.net',
'https://231787.xyz',
'https://25054128.xyz',
'https://3h.lv',
'http://hy-2.com',
'http://lanmaoyun.icu',
'http://sq9xy6.cpminig.com',
'http://qingyun.zybs.eu.org',
'http://www.kuaidog006.top',
'http://vpn.sudatech.store',
'http://needss.link',
'http://xn--4gqp1u.com',
'http://ch.louwangzhiyu.xyz',
'http://sulink.pro',
'http://xueyejiasu.com',
'http://47.243.59.73',
'http://569cdn.1010520.click',
'https://523qaweg246.pandafly.site',
'https://9bd4028e.ghelper.me',
'https://aaa.yunduanjc.top',
'https://awacloud.online',
'https://ch.cukug.website',
'https://dy.kuailejc.xyz',
'https://dy.naisicloud.xyz',
'https://huahe.link',
'https://jb.taipeicity.news',
'https://ly.ccwink.cc',
'https://pianyi.sub.sub.subsub123456789.com',
'https://pro.xn--l9qyaz082a.cn',
'https://qq.xlm.plus',
'https://sub.mogufan.com',
'https://sub.sanfen018.xyz',
'https://sub.tgzdyz2.xyz',
'https://sub.tuanzi.xyz',
'https://sub.xn--4gq62ffxz.net',
'https://sub.xn--4gqp1u.com',
'https://submit.xz61.cn:23443',
'https://www.dabai.in',
'https://youxiu5172.xiaofeixia.cfd',
'https://dash2.moonriver.one',
'https://cn.newbee888.cc',
'https://6.needss.one',
'https://xc1.shishi1.buzz',
'https://mgxiaowu.net',
'https://dabai.in',
'https://db01.in',
'https://hy-2.sbs',
'https://aa.dabai.in',
'https://api.heima2u.com',
'https://www.meigui168.net',
'https://cn.newbee.cyou',
'https://mgnet.vip',
'https://portal.speedyyun.com',
'https://s1.equinoxaa.com',
'https://www.f2ray.com',
'https://www.littleqqq.co',
'https://懒猫.com',
'https://www.z1z1.top',
'https://honven20.dgywzc.com',
'https://reurl.cc',
'https://cloud.speedypro.xyz',
'https://www.qlgq.top',
'https://www.v2ny.com',
'https://ikuuu.me',
'https://xn--iiq540h.com',
'https://jgjs02.com',
'https://xn--4gq62f52gdss.com',
'https://board.jike99.xyz',
'https://www.mojie.me',
'https://besnow.me',
'https://lksi.xyz',
'https://www.taishan.pro',
'https://zhu.suyun.bio',
'https://glados.space',
'https://tly.sh',
'https://sockboom.love',
'https://panel.keleofficial.com',
'https://daniu.e300daniu.top',
'https://klxq.djgskc.top',
'https://px.bt3.one',
'https://chy.fit',
'https://v3ssy.xyz',
'https://www.proxyvip.xyz',
'https://daxun.club',
'https://bcast.ink',
'https://b0chi.r-yu.me',
'https://cd520.xyz',
'https://www.aoxiangyun.top',
'https://www.mickey.business',
'https://sp.nfsq.me',
'https://cocolink.org',
'https://oukasou.xyz',
'https://www.aimacloud.info',
'https://user.xinna.co',
'https://nanmin.xyz',
'https://qiaoxbbq.com',
'https://mxwljsq.xyz',
'https://www.okvpn.cc',
'https://my.jetfast.dev',
'https://shandiandog.com',
'https://tagss04.pro',
'https://suo.yt',
'https://cdn.ednovas.org',
'https://qytvipaffcc04.qytvipaff.pro',
'https://fengwo.pro',
'https://love.52pokemon.cc',
'https://ocloudvpn.com',
'https://mly01.miaolianyun.my',
'https://px.xinyo.me',
'https://airport.raloar.top',
'https://xunlian.site',
'https://www.cacapex.com',
'https://a.kpyun.live',
'https://main.cute-cloud.de',
'https://cloud.jisuba.me',
'https://便宜机场.co',
'https://site01.stardad.lol',
'https://mogufan.com',
'https://app.cloudog.me',
'https://invite6.cht.taipei',
'https://app.gomeow.cloud',
'https://guobaotegong.me',
'https://jjz2.31465.cfd',
'https://a.0123456789.us.kg',
'https://a.opk.icu',
'https://569.2.passwallwall.life',
'https://aeda2.asa.lol',
'https://user.dafeiji.one',
'https://web2.dogssr.sbs',
'https://web2.52pokemon.cc',
'https://ni8.zxm.cc',
'https://sub.ssrsub.com',
'https://www.kuaidog010.top',
'https://mlshu.com',
'https://dash.bigcow.cc',
'https://www.fawncloud.one',
'https://cloud.speedyweb.xyz',
'https://z.luxury',
'https://askahh.com',
'https://powerwan.net',
'https://afun.la',
'http://web.nnpy.org',
'https://syyn.1.passwallwall.life',
'https://www11.henet.uk',
'https://ikuuu.pw',
'https://xn--wtq35pfyd55o.co',
'https://asa.lol',
'https://www.huaxia.cyou',
'https://newserver.t1i.top',
'https://ins.ins66.com',
'https://www.flymetothemoon.work',
'http://ov2rayo.top',
'http://17yxyy.cc',
'https://54fxp.xyz',
'https://haoba.cloud',
'https://mianmd.ninja',
'https://www.gogocloud.cyou',
'https://planb.cat',
'https://v.cheerfun.dev',
'https://www.cantonx.com',
'https://air.yoyoss.xyz',
'https://www.v2ssr.top',
'https://91yun.buzz',
'https://portal.buddhajumpsoverthewall.com',
'http://network2.magic-in-china.com',
'https://kedouair.top',
'http://kaxin.cc',
'https://www.wkyun1688.com',
'https://ssr.giize.com',
'https://home.wkyuns.xyz',
'https://air.misakano.eu.org',
'https://yhcvpn.xyz',
'https://www.starlink9527.xyz',
'https://starlink.to',
'https://bajie.info',
'https://marslink.org',
'https://www.marslink.cc',
'https://8rkt.xyz',
'https://miaona.xyz',
'https://api.dashsp.top',
'https://miaona.co',
'https://latiao.club',
'https://58sd.net',
'https://latiao.us',
'https://glados.one',
'https://glados.network',
'https://bityun.org',
'http://bityun.org',
'http://sub.chbjpw.mobi',
'https://88catnet.com',
'https://www.99catnet.com',
'https://www.58mdss.com',
'https://mdss.cloud', 
'https://m11.spwvpn.com',
'https://m2net.lol',
'https://m2net.sbs',









 )
#文件路径
update_path = "./sub/"
#所有的clash订阅链接
end_list_clash = []
#所有的v2ray订阅链接
end_list_v2ray = []
#所有的节点明文信息
end_bas64 = []
#获得格式化后的链接
new_list = []
#永久订阅
e_sub = ['']
#频道
urls =[]
#线程池
threads = []
#机场链接
plane_sub = ['']
#机场试用链接
try_sub = []
#获取频道订阅的个数
sub_n = -25
#试用节点明文
end_try = []

#获取群组聊天中的HTTP链接
def get_channel_http(url):
    headers = {
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://t.me/s/oneclickvpnkeys',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post(
        url, headers=headers)
    #print(response.text)
    pattren = re.compile(r'"https+:[^\s]*"')
    url_lst = pattren.findall(response.text)
    #print('获取到',len(url_lst),'个网址')
    #print(url_lst)
    return url_lst


#对bs64解密
def jiemi_base64(data):  # 解密base64
    # 对 Base64 编码后的字符串进行解码，得到字节字符串
    decoded_bytes = base64.b64decode(data)
    # 使用 chardet 库自动检测字节字符串的编码格式
    encoding = chardet.detect(decoded_bytes)['encoding']
    # 将字节字符串转换为字符串
    decoded_str = decoded_bytes.decode(encoding)
    return decoded_str

#判读是否为订阅链接
def get_content(url):
    #print('【获取频道',url,'】')
    url_lst = get_channel_http(url)
    #print(url_lst)
    #对链接进行格式化
    for i in url_lst:
        result = i.replace("\\", "").replace('"', "")
        if result not in new_list:
            if "t" not in result[8]:
                if "p" not in result[-2]:
                    new_list.append(result)
    #print(new_list)
    #print("共获得", len(new_list), "条链接")
    #获取单个订阅链接进行判断
    i = 1
    try:
        new_list_down = new_list[sub_n::]
    except:
        new_list_down = new_list[len(new_list) * 2 // 3::]
    #print("共获得", len(new_list_down), "条链接")
    #print('【判断链接是否为订阅链接】')
    for o in new_list_down:
        try:
            res = requests.get(o)
            #判断是否为clash
            try:
                skuid = re.findall('proxies:', res.text)[0]
                if skuid == "proxies:":
                    #print(i, ".这是个clash订阅", o)
                    end_list_clash.append(o)
            except:
                #判断是否为v2
                try:
                    #解密base64
                    peoxy = jiemi_base64(res.text)
                    #print(i, ".这是个v2ray订阅", o)
                    end_list_v2ray.append(o)
                    end_bas64.extend(peoxy.splitlines())
                    
                #均不是则非订阅链接
                except:
                    #print(i, ".非订阅链接")
                    pass
        except:
            #print("第", i, "个链接获取失败跳过！")
            pass
        i += 1
    return end_bas64

#写入文件
def write_document():
    if e_sub == [] or try_sub == []:
        print("订阅为空请检查！")
    else:
        #永久订阅
        random.shuffle(e_sub)
        for e in e_sub:
            try:
                res = requests.get(e)
                proxys=jiemi_base64(res.text)
                end_bas64.extend(proxys.splitlines())
            except:
                print(e,"永久订阅出现错误❌跳过")
        print('永久订阅更新完毕')
        #试用订阅
        random.shuffle(try_sub)
        for t in try_sub:
            try:
                res = requests.get(t)
                proxys=jiemi_base64(res.text)
                end_try.extend(proxys.splitlines())
            except Exception as er:
                print(t,"试用订阅出现错误❌跳过",er)
        print('试用订阅更新完毕',try_sub)
        #永久订阅去重
        end_bas64_A = list(set(end_bas64))
        print("去重完毕！！去除",len(end_bas64) - len(end_bas64_A),"个重复节点")
        #永久订阅去除多余换行符
        bas64 = '\n'.join(end_bas64_A).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #试用去除多余换行符
        bas64_try = '\n'.join(end_try).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #获取时间，给文档命名用
        t = time.localtime()
        date = time.strftime('%y%m', t)
        date_day = time.strftime('%y%m%d', t)
        #创建文件路径
        try:
            os.mkdir(f'{update_path}{date}')
        except FileExistsError:
            pass
        txt_dir = update_path + date + '/' + date_day + '.txt'
        #写入时间订阅
        file = open(txt_dir, 'w', encoding='utf-8')
        file.write(bas64)
        file.close()       
        
        #减少获取的个数
        r = 1
        length = len(end_bas64_A)  # 总长
        m = 8  # 切分成多少份
        step = int(length / m) + 1  # 每份的长度
        for i in range(0, length, step):
            print("起",i,"始",i+step)
            zhengli = '\n'.join(end_bas64_A[i: i + step]).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
            #将获得的节点变成base64加密，为了长期订阅
            obj = base64.b64encode(zhengli.encode())
            plaintext_result = obj.decode()
            #写入长期订阅
            file_L = open("Long_term_subscription"+str(r), 'w', encoding='utf-8')
            file_L.write(plaintext_result)
            r += 1
        #写入总长期订阅
        obj = base64.b64encode(bas64.encode())
        plaintext_result = obj.decode()
        file_L = open("Long_term_subscription_num", 'w', encoding='utf-8')
        file_L.write(plaintext_result)
        #写入试用订阅
        obj_try = base64.b64encode(bas64_try.encode())
        plaintext_result_try = obj_try.decode()
        file_L_try = open("Long_term_subscription_try", 'w', encoding='utf-8')
        file_L_try.write(plaintext_result_try)
        #写入README
        with open("README.md", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        now_time = datetime.datetime.now()
        TimeDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for index in range(len(lines)):
            try:
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
                    lines.pop(index+4)
                    lines.pop(index+4)
                    lines.insert(index+4, f'Updata：`{TimeDate}`\n')
                    lines.insert(index+4, f'### Try the number of high-speed subscriptions: `{len(try_sub)}`\n')
                if lines[index] == '>Trial subscription：\n': # 目标行内容
                    lines.pop(index)
                    lines.pop(index)
                """
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
                """
            except:
                #print("写入READ出错")
                pass
        #写入试用订阅
        for index in range(len(lines)):
            try:
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        #lines.insert(index+n-1, f'\n>')
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
            except:
                print("写入试用出错")
        
        with open("README.md", 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            f.write(data)
        print("合并完成✅")
        try:
            numbers =sum(1 for _ in open(txt_dir))
            print("共获取到",numbers,"节点")
        except:
            print("出现错误！")
        
    return

#获取clash订阅
def get_yaml():
    print("开始获取clsah订阅")
    urls = []
    n = 1
    for i in urls:
        response = requests.get(i)
        #print(response.text)
        file_L = open("Long_term_subscription" + str(n) +".yaml", 'w', encoding='utf-8')
        file_L.write(response.text)
        file_L.close()
        n += 1
    print("clash订阅获取完成！")

#获取机场试用订阅
def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            form_data = {
                'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                'password': 'autosub_v2b',
                'invite_code': '',
                'email_code': ''
            }
            if current_url == 'https://xn--4gqu8thxjfje.com' or current_url == 'https://seeworld.pro'  or current_url == 'https://www.jwckk.top'or current_url == 'https://vvtestatiantian.top':
                try:
                    fan_res = requests.post(
                        f'{current_url}/api/v1/passport/auth/register', data=form_data, headers=header)
                    auth_data = fan_res.json()["data"]["auth_data"]
                    #print(auth_data)
                    fan_header = {
                        'Origin': current_url,
                        'Authorization': ''.join(auth_data),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                        'Referer': current_url,
                    }
                    fan_data = {
                        'period': 'onetime_price',
                        'plan_id': '1',
                    }
                    fan_res_n = requests.post(
                        f'{current_url}/api/v1/user/order/save', headers=fan_header, data=fan_data)
                    #print(fan_res_n.json()["data"])
                    fan_data_n = {
                        'trade_no':fan_res_n.json()["data"],
                        #'method': '1',
                    }
                    fan_res_pay = requests.post(
                        f'{current_url}/api/v1/user/order/checkout', data=fan_data_n, headers=fan_header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={fan_res.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as result:
                    print(result)
                    break
            else:
                try:
                    response = requests.post(
                        current_url+V2B_REG_REL_URL, data=form_data, headers=header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as e:
                    print("获取订阅失败",e)
            i += 1

            
  
def get_kkzui():
    # ========== 抓取 kkzui.com 的节点 ==========
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://kkzui.com/jd?orderby=modified",headers=headers)
        article_url = re.search(r'<h2 class="item-heading"><a href="(https://kkzui.com/(.*?)\.html)"',res.text).groups()[0]
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'<p><strong>这是v2订阅地址</strong>：(.*?)</p>',res.text).groups()[0]
        print(sub_url)
        e_sub.append(sub_url)
        print("获取kkzui.com完成！")
    except:
        print("获取kkzui.com失败！")
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://www.cfmem.com/search/label/free",headers=headers)
        article_url = re.search(r"https?://www\.cfmem\.com/\d{4}/\d{2}/\S+v2rayclash-vpn.html",res.text).group()
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'>v2ray订阅链接&#65306;(.*?)</span>',res.text).groups()[0]
        print(sub_url)
        try_sub.append(sub_url)
        e_sub.append(sub_url)
    except Exception as e:
        print(e)
        
    
if __name__ == '__main__':
    print("========== 开始获取机场订阅链接 ==========")
    get_sub_url()
    print("========== 开始获取kkzui.com订阅链接 ==========")
    get_kkzui()
    print("========== 开始获取频道订阅链接 ==========")
    for url in urls:
        #print(url, "开始获取......")
        thread = threading.Thread(target=get_content,args = (url,))
        thread.start()
        threads.append(thread)
        #resp = get_content(get_channel_http(url))
        #print(url, "获取完毕！！")
    #等待线程结束
    for t in tqdm(threads):
        t.join()
    print("========== 准备写入订阅 ==========")
    res = write_document()
    clash_sub = get_yaml()
    print("========== 写入完成任务结束 ==========")
