import requests
import sys
import io
import json
names=[]
id=[]
h=requests.get('http://i.xue.taobao.com/json/asynOutline.do?courseId=81929&_ksTS=1525316883405_135&callback=').text
js=json.loads(h)
for j in range(0,len(js["data"]['chapters'])):
    for i in range(0,len(js["data"]['chapters'][j]['sections'])):
        names.append(js["data"]['chapters'][j]['sections'][i]['title'])
        id.append(js["data"]['chapters'][j]['sections'][i]['resources'][0]['id'])



proxies = {
		"http": "http://127.0.0.1:8080",
		"https": "http://127.0.0.1:8080",
	}
cookie="t=99fba40d69e32c8615608d117da226fe; cna=aK26EjGs234CAXPij0odfNEH; isg=BElI2hfldxQx9ws5nGnkIvncW3ZjPj-v51pR_-u_sDBtMn5EMuCemSokcBaEcdUA; l=Anp6khzBl-iOEmJJhECMyM/uyqucK/4F; thw=cn; um=A502B1276E6D5FEF082804C5DF34B1197CEB2474384E53430504264BD6E8BFDF2686A66EC7012521CD43AD3E795C914CBBE507231AAF86F59098BA24697CA3C9; tracknick=tb050112892; UM_distinctid=16254052d96e9b-0b589addd811ef8-4c322073-1fa400-16254052d98f2c; miid=776152677720350247; _m_h5_tk=080034d1072ca1672dd7107cd93eb5af_1524906444991; _m_h5_tk_enc=df281c7dcc86b8c2b903759421d61e1b; uc3=nk2=F5RFhSvAvT%2F93%2B4%3D&id2=UNiGnNJvt%2BG73Q%3D%3D&vt3=F8dBz44nTSK8OiRKD3g%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; lgc=tb050112892; mt=np=&ci=0_1; _cc_=URm48syIZQ%3D%3D; tg=4; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=false&pas=0&cookie14=UoTeO8kKcSJvaQ%3D%3D&tag=8&lng=zh_CN; cookie2=3c92a64455fe4aa04fbe48d7a96571fb; v=0; _tb_token_=e5ea8b63e3ee6; existShop=MTUyNTQyNTg0MQ%3D%3D; dnk=tb050112892; csg=6bf075ac; skt=8226f6aa4100ddfc; sg=207; cookie1=BxJOPHXCavefIC25%2Fqds0zErLbYNBxguGy0t1L9e2xU%3D; unb=3828948260; _l_g_=Ug%3D%3D; _nk_=tb050112892; cookie17=UNiGnNJvt%2BG73Q%3D%3D"
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
cookies={}
for line in cookie.split(';'):
    name,value=line.strip().split('=',1)
    cookies[name]=value
for k in range (24,len(id)):
 url='http://v.xue.taobao.com/json/asynResource.do?courseId=81929&resourceId='+ str(id[k]) +'&resourceType=1&sectionId=2877098&last=false&liveToolType=0&_ksTS=1525314449212_404&callback='
 li=requests.get(url,cookies=cookies).text
 list=json.loads(li)
 url1= list["data"]["resource"]["extObj"]["videoPlayInfo"]["androidPadV23Url"]["hd"]+'?auth_key='+list["data"]["resource"]["authority"]["authKey"]
 try:
	 path = 'D:/pythone study/taobao/'+str(k)+'.%s.mp4'%names[k]
	 pic = requests.get(url1, headers=headers)
	 data=pic.content
	 with open(path, 'wb') as f:
		f.write(data)
		f.close
		print("ok..."+str(k))
 except:
	 print("no..."+str(k))


