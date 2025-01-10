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
'http://17yxyy.cc',
'http://1run.vip',
'http://38.AL',
'http://406.tzwlwm.cn:8002',
'http://9o9.top:880',
'http://api.hpyjc.top',
'http://app.gougouvpn.xyz:88',
'http://bityun.org',
'http://c.33pt.top:80',
'http://carterzheng.synology.me:8008',
'http://cc.legeth.cc',
'http://clash.huiwg.cn',
'http://clash.huiwg.cn:80',
'http://clashe.eu.org:80',
'http://dash.fscloud.cc',
'http://dash.legeth.com',
'http://dishujichang.xyz',
'http://dls.frpfrp.xyz',
'http://dls.frpfrp.xyz:80',
'http://dy.fengyetv.top',
'http://fetchjiedian.feisu360.xyz',
'http://free.dsdog.tk:80',
'http://free.iam7.tk',
'http://fuqiang.reot.top',
'http://gz.lauwnas.fun:22580',
'http://haohaoxiong.myqnapcloud.com:12580',
'http://hk.dstds.top',
'http://home.54bb.com:12580',
'http://hpyjc.top',
'http://ja97.hwqwl.com:8089',
'http://jeplove.f3322.net:12580',
'http://jeplove.wicp.net:12580',
'http://json.cloud94.cn:12123',
'http://kaxin.cc',
'http://kiwi2.cgweb.top',
'http://klausvpn.posyao.com',
'http://legeth.eatuo.com',
'http://liuxing.asuscomm.com:3003',
'http://longying.us.kg',
'http://mail.vilaan.com:28080',
'http://msvpn.gougouvpn.xyz:88',
'http://nanbei.buzz',
'http://nanbei.cloud',
'http://network2.magic-in-china.com',
'http://one.bblinks.top',
'http://onefall.top',
'http://origin.legeth.com',
'http://ov2rayo.top',
'http://paoche.ga',
'http://pc.adlionvm.tk:33100',
'http://pi.scntvb.ml:8080',
'http://pp.dcd.one:80',
'http://proxy.fldhhhhhh.top',
'http://proxypool.assists.ai:80',
'http://proxypool.fly.dev:80',
'http://proxypool.kengro.cn',
'http://proxypool.kengro.cn:80',
'http://proxypool.leuliu.com:80',
'http://proxypoolabc.andyc.eu.org:80',
'http://qingyunti.cc',
'http://rmtzx.cf:12580',
'http://rot.9o9.top:880',
'http://sansui233.com',
'http://sansui233.com:80',
'http://ssr.wujietest.top:8088',
'http://sub.1921.eu.org',
'http://sub.chbjpw.mobi',
'http://sub.networkline.top',
'http://sub.networkline.top:80',
'http://t4.xiaogv.cn',
'http://tg.anyoug.com',
'http://tt4.xiaogv.cn:12580',
'http://vc.4xm.cn:807',
'http://vpc.llwe.ga',
'http://vyy.idsduf.com',
'http://www.caoliang.top:12580',
'http://www.ckcloud.xyz',
'http://www.fanrr.xyz',
'http://www.paopao.dog',
'http://www.sansui233.com:80',
'http://www.timefish.xyz',
'http://xqcloud.net',
'http://xqz0.vip:12580',
'http://xqz0.vip:12582',
'http://ypgt.tk:12580',
'http://ypll.xyz:80',
'http://yunwu.sbs',
'http://zhaozhanzhan520.imwork.net:5900',
'http://zixibar.net:12580',
'http://zq.jasonml.ml',
'https://000000online.life',
'https://01.hpv01.top',
'https://1.114524.xyz',
'https://1.kepayun.tech',
'https://1.vyunyun.top',
'https://12123.org',
'https://13x.one',
'https://1vpn.sbs',
'https://1ytcom01.1yunti.net',
'https://1yunti.com',
'https://22.lownet.xyz',
'https://22044.xyz',
'https://223360.xyz',
'https://233dmt.com',
'https://2lands.me',
'https://361361.xyz',
'https://38.6.227.114',
'https://38.al',
'https://4.ni8.me',
'https://4.ni8.pro',
'https://4100594342.xn--jbyq16e.xyz',
'https://520748.xyz',
'https://520s.pro',
'https://54fxp.xyz',
'https://58.35.85.247:8084',
'https://58rocket.com',
'https://58sd.net',
'https://5nnn.top',
'https://666666222.xyz',
'https://67889.pro',
'https://6b.lmnw1.top',
'https://74.226.193.95',
'https://88catnet.com',
'https://8rkt.xyz',
'https://8yun.me',
'https://900999.xyz',
'https://911vp.cc',
'https://91b06.cc',
'https://91fjc80.cc',
'https://91yun.buzz',
'https://98kjc.top',
'https://a.aik88.top',
'https://a.fsyun.xyz',
'https://a.kepayun.lol',
'https://a.kepayun.tech',
'https://a.kepayun.xyz',
'https://a.kpyun.live',
'https://a.yousu.cc',
'https://a01.fxscloud.com',
'https://a1.darkforest.cloud',
'https://a123.buzz',
'https://a72.aaa7.info',
'https://abc.noseisei.com',
'https://abyssvpn.com',
'https://ai.totwo.link',
'https://ai.totwo.top',
'https://aikx.me',
'https://air.aptlive.org',
'https://air.misakano.eu.org',
'https://air.ssgzx.com',
'https://air.yoyoss.xyz',
'https://airport.lemonying.cfd',
'https://airport.raloar.top',
'https://alandegtr.com',
'https://alicenetwork.cloud',
'https://andaofu.xyz',
'https://antlink.cc',
'https://antlink.icu',
'https://anydoor.xyz',
'https://anyland01.com',
'https://api.256600.xyz',
'https://api.dashsp.top',
'https://api114514.nuwaa.rest',
'https://apidagecloud.com',
'https://app.birds.hk',
'https://app.cloudlion.me',
'https://app.cloudog.me',
'https://app.gomeow.cloud',
'https://app.legeth.cc',
'https://app.lwjyj.com',
'https://arisaka.io',
'https://asa.lol',
'https://atcskylink.com',
'https://awsgcp.tk',
'https://axixw.cc',
'https://ayouok.online',
'https://azi.azzico.cc',
'https://azz.azzico.com',
'https://b.clmvip.com',
'https://b.etime.vip',
'https://b.kepayun.lol',
'https://b.kepayun.tech',
'https://b.xiaow.cc',
'https://b.yousu.cc',
'https://bailian.site',
'https://bajie.info',
'https://bajie.pw',
'https://bbjc.xyz',
'https://bityun.org',
'https://bkcloud.cloud',
'https://blackholeservices.com',
'https://blog.xiquedao.top',
'https://blueseago.tk:8443',
'https://boy.mianfeiyun.xyz',
'https://bp.wbno1.xyz',
'https://bpjc.art',
'https://bpjc.lol',
'https://bplink.xyz',
'https://breakwalls.us',
'https://bscloud.xyz',
'https://bt3.one',
'https://by.yunduanjc.top',
'https://c.33pt.top:443',
'https://c.kepayun.tech',
'https://c.yousu.cc',
'https://c03831cb-738b-4e2c-976e-5feff6408102.id.repl.co',
'https://cainiao168.top',
'https://cainiao172.top',
'https://cainiao181.top',
'https://cainiao182.top',
'https://cainiao183.top',
'https://cainiao999.top',
'https://catclaw.cloud',
'https://cf.tsqdgfly.vip',
'https://cfyun01.sbs',
'https://changyouvpn.top',
'https://chaozhijc.xyz',
'https://chiguayun.com',
'https://chiguayun.net',
'https://chiguayun.org',
'https://chinayyds.xyz',
'https://chukou.co',
'https://ciyy.cc',
'https://ciyy.one',
'https://cla.floridajc.uk',
'https://clash.huiwg.cn',
'https://clash.huiwg.cn:443',
'https://clash.myvm.cc',
'https://clash.quain.top',
'https://clashe.eu.org:443',
'https://client.1314.help',
'https://client.3i.lol',
'https://client.huaye.buzz',
'https://client.okaycloud.top',
'https://client.xiaoguapi.top',
'https://clmd.me',
'https://clmd.pro',
'https://cloud.9hz.club',
'https://cloud.fufudog.com',
'https://cloud.gyyun.top',
'https://cloud.halo.do',
'https://cloud.mianfeiyun.xyz',
'https://cloud.xn--pbt38zg4v.com',
'https://cloud.yydschina.top',
'https://cloud.yyts.cfd',
'https://cloud.柠萌宝.com',
'https://cloudandfire.org',
'https://cloudcat.top',
'https://cloudlion.me',
'https://cloudog.us.kg',
'https://cnrocket.top',
'https://cococloud.online',
'https://colacloud.net',
'https://conyss.net',
'https://coo.lol',
'https://cr.shuiyunxuan.pw',
'https://cssdoctor.pages.dev',
'https://csyun.t1csyun.shop',
'https://csyun.xyz',
'https://cxk.lol',
'https://cy.z49.top',
'https://d.kepayun.xyz',
'https://d1.yogurt.icu',
'https://daishujiasu.club',
'https://daishujiasu.com',
'https://darkforest.cloud',
'https://dash.996cloud.top',
'https://dash.catnet.uk',
'https://dash.fscloud.cc',
'https://dash.fxscloud.com',
'https://dash.minizz.online',
'https://dashboard.zrj222.xyz',
'https://db.shellnet.net',
'https://ddddd.site',
'https://dhh.lol',
'https://directstore.kakocloud.pro',
'https://dishujichang.top',
'https://dishuyun.top',
'https://dk3.yunxiangvip.mom',
'https://dk4.yunxiangvip.mom',
'https://dls.frpfrp.xyz',
'https://dnsss.top',
'https://dog.ssrdog.com',
'https://dogssr.sbs',
'https://douyun.us',
'https://drive.namichan.site',
'https://drive.namichan.site:9000',
'https://dxmax.net',
'https://dy.fengyetv.top',
'https://echonetwork.club',
'https://egayun.live',
'https://eggtartcloud.shop',
'https://elfgate.dev',
'https://ep.0318.cyou',
'https://f.fengwo.online',
'https://f.kepayun.xyz',
'https://f.nekov.org',
'https://f.wwwq.net',
'https://fanqiang88.top',
'https://fastestcloud.xyz',
'https://fastlink.me',
'https://fatcatcloud.cc',
'https://fatmiaoo.com',
'https://fb.6bcloud.top',
'https://feiyucloud.top',
'https://fengcheyun.xyz',
'https://fengchi.buzz',
'https://fengwo.online',
'https://fengwo.pro',
'https://fengwo.sdtsd.cn',
'https://fengzg.net',
'https://fetchjiedian.feisu360.xyz',
'https://flybit.vip',
'https://forest-cn.com',
'https://forest-network.com',
'https://fpacecloud.com',
'https://free.24th.link:443',
'https://free.346492.xyz',
'https://free.colacloud.free.hr',
'https://free.dsdog.tk:443',
'https://free.iam7.tk',
'https://free.jingfu.cf',
'https://free.ninecloud.co',
'https://free.suwas.xyz',
'https://free.zlcom.ml',
'https://freeair.colacloud.free.hr',
'https://freebird.free886.site',
'https://freecat.cloud',
'https://freeflyingcloud.com',
'https://freegfw.top',
'https://freejc.xyz',
'https://ftzaffcom01.fliggyaff.xyz',
'https://ftzcc01.fliggycloud.pro',
'https://fuli.yuwenle.vip',
'https://furina.world',
'https://g.kepayun.xyz',
'https://g01.info',
'https://g9s8.miqi8.xyz',
'https://gd.kaxinzx.cc',
'https://gfw.best',
'https://gg.mqs.xyz',
'https://glados.network',
'https://glados.one',
'https://glados.space',
'https://gogocloud.top',
'https://googo.us',
'https://gos.wiki',
'https://gougouvpn.top',
'https://guanwang.me',
'https://guobaotegong.me',
'https://gyyun.top',
'https://haimian.icu',
'https://haitunyun.online',
'https://haoba.cloud',
'https://hd.pangzi5.top',
'https://hdyun.cc',
'https://hi.lmnw1.top',
'https://hjhjhj.hjdns.top',
'https://hjvip.cc',
'https://hk.bros.us.kg',
'https://hk.dstds.top',
'https://hk.dstds.top:443',
'https://hktix.net',
'https://hmkj3.com',
'https://home.wkyuns.xyz',
'https://hosts.daohangs.xyz',
'https://houduan.fastss.de',
'https://houtai.site',
'https://hperformence.top',
'https://hpyjc.top',
'https://huajic.pro',
'https://huotuichang.top',
'https://hx666.info',
'https://hxlm.io',
'https://hxlm.org',
'https://hy-2.com',
'https://iepl.io',
'https://ieplcloud.net',
'https://ikun.co.uk',
'https://ikunvpn.com',
'https://inlook.me',
'https://ins77.link',
'https://jc.886811.xyz',
'https://jich.tih2.eu.org',
'https://jichang.123417.xyz',
'https://jichang.jinsanjiaohs.com',
'https://jihuyun.icu',
'https://jileiyun.top',
'https://jileiyun.us.kg',
'https://jindouyun88.life',
'https://jisovpn.site',
'https://jixingwangluo.top',
'https://jjcloud.xyz',
'https://jjz.31465.cfd',
'https://jkcloud.net',
'https://jk-cloud.net',
'https://juanwang.store',
'https://kaikaixinxin.me',
'https://kaolacloud.site',
'https://kapoksub.com',
'https://kcjb.org',
'https://kedouair.top',
'https://kepayun.xyz',
'https://kfccloud.cc',
'https://kitty.works',
'https://kiwi2.cgweb.top',
'https://kiwi2.cgweb.top:443',
'https://klausvpn.posyao.com',
'https://kqvpn.com',
'https://kr521.dynv6.net:9041',
'https://krelenet.com',
'https://kscloud.xyz',
'https://ktcat.ru',
'https://ktmcloud.shop',
'https://ktmcloud.top',
'https://kuailejc.xyz',
'https://kuaiqiangshou.xyz',
'https://lagarbi.top',
'https://lanxingyun.com',
'https://laomaoyun.me',
'https://latiao.buzz',
'https://latiao.club',
'https://latiao.us',
'https://laxcity.pages.dev',
'https://lbei.net',
'https://lcloud.wiki',
'https://leadingto.cloud',
'https://leflycloud.com',
'https://leka.one',
'https://lemontea.shop',
'https://lemshow.top',
'https://leseyun.com',
'https://liangyuandian.club',
'https://limeis.best',
'https://linghun1.com',
'https://linghunyun.com',
'https://linzexu.pro',
'https://littlerocket.cc',
'https://liulangdiqiu.cc',
'https://llgjc.shop',
'https://lonan.gay',
'https://lovenao.tk',
'https://ludou.me',
'https://lx.liuxing2023.top',
'https://ly.lingya666.xyz',
'https://lzyjc.xyz',
'https://m.clmvip.com',
'https://magic.tegin.xyz',
'https://magicm.cc',
'https://magicm.link',
'https://magicm.sbs',
'https://magicm.top',
'https://main.cute-cloud.de',
'https://maple.icu',
'https://marslink.org',
'https://mdss.cloud',
'https://metacloud.eu.org',
'https://mg801.cc',
'https://mg803.cc',
'https://mgypog.xyz',
'https://mianguan.xyz',
'https://mianmd.ninja',
'https://miaona.co',
'https://miaona.org',
'https://miaona.xyz',
'https://mikadonet.xyz',
'https://mingtian.lol',
'https://minizz.online',
'https://misakanetwork.top',
'https://mitutu.cc',
'https://mkl.ikorg.cc',
'https://mochizuki.top',
'https://mogufan.com',
'https://mojie.best',
'https://mojie.cyou',
'https://mojie.info',
'https://mojie.link',
'https://mojie.me',
'https://mojie.pw',
'https://moluo.cloud',
'https://moyucloud.com',
'https://mpddt.top',
'https://mro5n.no-mad-world.club',
'https://my.catfaka.com',
'https://my.kei.one',
'https://my.legeth.com',
'https://my.pianyi.info',
'https://myaqiqi.top',
'https://myko.buzz',
'https://myxiongadi.top',









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
