from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template

app = Flask(__name__)




@app.route('/')
def home():
    l=[]
    search="chicken"
    source=requests.get("https://www.shwapno.com/products/meat--fish-meat-"+search+"/other/broiler-chicken-without-skin-per-kg/pid-12100222.aspx").text
    soup=BeautifulSoup(source,'lxml')
    title="Boiler Chicken Without Skin"
    price_section=soup.select('.productprices >span > label')
    price=price_section[1].text
    price_amounts=soup.select('.productprices >span .sp_amt')
    price_amount=price_amounts[0].text
    
    d={}
    d['title']=title
    d['price']=price
    d['price_amount']=price_amount
    l.append(d)
    newli=[]
    url=requests.get("https://chaldal.com/broiler-chicken-skin-on-net-weight-50-gm-1-kg").text
    soup=BeautifulSoup(url,'lxml')
    price_section_chal=soup.select('.discountedPrice > span >span')
    price_chal=price_section_chal[0].text
    title_chal="Boiler Chicken"
    newdi={}
    newdi['title_chal']=title_chal
    newdi['price_chal']=price_chal
    newli.append(newdi)
    


    baseurl=requests.get("https://www.shwapno.com/products/meat--fish-meat-chicken/other/broiler-chicken-with-skin-per-kg/pid-12100234.aspx").text
    soup=BeautifulSoup(baseurl,'lxml')
    title="Boiler Chicken With Skin"
    price_amounts=soup.select('.productprices .offer .sp_amt')
    price=price_amounts[0].text
    li3=[]
    di3={}
    di3['title']=title
    di3['price']=price
    li3.append(di3)

    return render_template('index.html',products=l,chal_products=newli,skin_products=li3)









    









    
    

app.run(debug=True)    

   