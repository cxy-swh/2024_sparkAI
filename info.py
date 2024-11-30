import requests
import urllib3
urllib3.disable_warnings()
cookie = {
    "Hm_lvt_55381c1b672ee8bc06b3d5d96941ed4f":"1732382515",
    "Hm_lpvt_55381c1b672ee8bc06b3d5d96941ed4f":"1732382515",
    "HMACCOUNT":"39E03057383EFA7E",
}
hard = {
    'referer': 'https://ai.sparkaigf.com/sparkai/admin/',
    'x-website-domain': 'ai.sparkaigf.com',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWQiOjIsImVtYWlsIjoiZGVmYXVsdEFkbWluQHNwYXJrYWlnYy5jb20iLCJyb2xlIjoiYWRtaW4iLCJvcGVuSWQiOiIiLCJjbGllbnQiOm51bGwsImlhdCI6MTczMjM4MjU0NCwiZXhwIjoxNzMyOTg3MzQ0fQ.XajIxT2jDcg1Wd53F_-ID0aPVeJYxTe2iBfhaIIonKY',
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
page_cust = input("第几页数据:")
params = {
    "userId":"",
    "platform":"",
    "status":"",
    "page":page_cust,
    "size":"15",
}
reponse = requests.get(
    url="https://ai.sparkaigf.com/api/order/queryAll?",
    headers=hard,
    cookies=cookie,
    params=params,
    verify=False,
).json()
for i in reponse['data']['rows']:
    id = i['id']
    name = i['userInfo']['username']
    orderId = i['orderId']
    email = i['userInfo']['email']
    goodsInfo_name = i['goodsInfo']['name']
    price = i['price']
    count = i['count']
    paydAt = ''
    if i['paydAt']:
        paydAt = f"成交时间 {i['paydAt']}"
    else:
        paydAt = "未支付"
    print(id, name, f'订单编号:{orderId}', f'邮箱:{email}', goodsInfo_name,f'{price}￥',f'{count}件',paydAt)