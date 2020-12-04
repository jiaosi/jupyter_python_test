

import requests

import time

##博时黄金ETF联接C

file_dir='/root/mydir/jupyter_python_test/'

url='http://api.fund.eastmoney.com/f10/lsjz'

endDate=time.strftime("%Y-%m-%d", time.localtime()) 

params={

'callback':'jQuery18304523957823296829_1606898055423',
'fundCode':'002611',
'pageIndex':'1',
'pageSize':'223',
'startDate':'2019-12-31',
'endDate': endDate,
'_':'1606898055423'

}

header={
 'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'intellpositionL=1079.19px; intellpositionT=755px; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; st_si=79614767262546; st_asi=delete; EMFUND0=null; EMFUND8=12-02%2015%3A53%3A44@%23%24%u535A%u65F6%u9EC4%u91D1ETF@%23%24159937; qgqp_b_id=abf761fbf3995ba629c5948a693b2a76; EMFUND9=12-02 15:56:29@#$%u535A%u65F6%u9EC4%u91D1ETF%u8054%u63A5C@%23%24002611; st_pvi=03515867673348; st_sp=2020-08-20%2015%3A10%3A00; st_inirUrl=https%3A%2F%2Fwww.google.com%2F; st_sn=7; st_psi=20201202163737300-0-0411983924',
'Host':'api.fund.eastmoney.com',
'Referer':'http://fundf10.eastmoney.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'   
}

resp=requests.get(url,params,headers=header)



def save_resp(json_data,file_name):
    with open(file_dir+file_name+'.json', mode='w', encoding='utf-8') as file:
        file.write(json_data)

#def get_json_file(file_name):
#    with open(file_name+'.json', mode='r', encoding='utf-8') as file:
#        return json.loads(file.read())

save_resp(resp.text,'gold')

##汇率
currency_url='http://www.chinamoney.com.cn/ags/ms/cm-u-bk-ccpr/CcprHisNew'

header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

params={
    'startDate':'2019-12-31',
'endDate':endDate,
'currency':'CNY/DKK,EUR/CNY,CHF/CNY,CNY/SEK',
    'pageNum': 1,
    'pageSize': 100000
}

resp=requests.post(currency_url,headers=header,params=params)

save_resp(resp.text,'currency')

print('finish ', endDate)
