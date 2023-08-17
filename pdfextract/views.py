import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from tractor.settings import STATICFILES_DIRS
from .forms import UrlForm
from .models import Url
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# import aspose.words as aw
from PIL import Image
from .models import Url
#from django.shortcuts import render

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests
from bs4 import BeautifulSoup as bs
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
import django
django.setup()


# Create your views here.
def index(request):
    form = UrlForm()
    return render(request, 'pdfextract/pdfextract_main.html', {'form':form})

def storage(request):
    if request.user.is_authenticated:
        print("hi")
        page = request.GET.get('page', '1')
        kw = request.GET.get('kw', '')
        url_list = Url.objects.order_by('-create_date')           
        if kw:
            url_list = url_list.filter(
                Url(link__icontains=kw) | 
                Url(date__icontains=kw) |  
                Url(comment__icontains=kw) |  
                Url(user_id__icontains=kw) 
            ).distinct()
        paginator = Paginator(url_list, 10) 
        page_obj = paginator.get_page(page)
        context = {'url_list': page_obj, 'page': page, 'kw': kw}
        return render(request, 'pdfextract/pdfextract_storage.html', context)
    else:
        return render(request, 'user/login.html')

def create(request):
    if request.method == 'POST' :
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.pdfpath = STATICFILES_DIRS[0] + "\\" + str(url.id) #사용자 id

            craw_data_dict = craw(url.url)
            for item in craw_data_dict:
                if url.keyword in item['comment']:    
                    url_item=Url()          
                    url_item.url=item['link']
                    url_item.user_id=item['user_id']
                    url_item.date=item['date']
                    url_item.comment = item['comment']
                    url_item.pdfpath = url.pdfpath
                    url_item.category = url.category
                    url_item.keyword = url.keyword
                    url_item.save()

        return HttpResponseRedirect('/pdfextract/storage/')
>>>>>>> d051de3971e0f9f08cbb239bebf1af48ea61e36e
    else:
        return render(request, 'user/login.html')
    
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UrlForm(request.POST)
            if form.is_valid():
                url = form.save(commit=False)
                url.pdfpath = STATICFILES_DIRS[0] + "\\" + str(url.id) #사용자 id

                craw_data_dict = craw(url.url)
                for item in craw_data_dict:
                    if url.keyword in item['comment']:    
                        url_item=Url()          
                        url_item.url=item['link']
                        url_item.user_id=item['user_id']
                        url_item.date=item['date']
                        url_item.comment = item['comment']
                        url_item.pdfpath = url.pdfpath
                        url_item.category = url.category
                        url_item.keyword = url.keyword
                        url_item.currentuser = request.user
                        url_item.save()
            return HttpResponseRedirect('/pdfextract/storage/')
        else:
            form = UrlForm()
            return render(request, 'pdfextract/pdfextract_main.html', {'form':form}) 
    else:
        return render(request, 'user/login.html')
    
def delete(request,pk):
    url = get_object_or_404(Url,id=pk)
    if request.user.is_authenticated:
        url.delete()
        return HttpResponseRedirect('/pdfextract/storage/')
    return HttpResponseRedirect('/pdfextract/storage/')


def extract(request):
    if request.method == "POST" and 'btn_extract' in request.POST:
        i = request.POST.getlist('box')[0]
        url = Url.objects.get(id=i) #id에 맞는 url 값
        p = Url.objects.get(id=i).pdfpath
        d = Url.objects.get(id=i).dflag
        print(d)

        userpath = p + "\\" #C:\projects\mysite\static\None\
        jpgpath = userpath + i

        if d == False :
            if not os.path.exists(userpath):
                os.mkdir(userpath)
            print(d)

            getPNG(str(url)) #전체 화면 캡쳐
            filepath = editPNG(jpgpath) #png -> pdf 변환

            url.pdfpath = filepath #db update
            url.dflag = True
            url.save()

            return download(filepath)
        else:       
            return download(p)
    else : HttpResponseRedirect('/pdfextract/storage/')

def getPNG(url):
    URL = url

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True

    #chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    totalWidth = driver.execute_script("return document.body.offsetWidth")
    totalHeight = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size("1480", totalHeight)
    sleep(3)

    driver.find_element(By.TAG_NAME, 'body').screenshot('fullshot.png')
    driver.quit()
    
    # editPNG(filename,path,id)
    #getPDF(filename)
    print("getPNG END")

    return HttpResponseRedirect('/pdfextract/storage/')

def editPNG(path):
    image1 = Image.open('fullshot.png')
    imag1_size = image1.size

    h = int(imag1_size[1]/4)
    
    for i in range(0,4):
        f= path + str(i) +'.png'
        print(f)
        area = (0, h*i, 1480, h*(i+1))
        crop_image = image1.crop(area)

        crop_image.save(f)
        
    img1 = Image.open(path +'0.png')
    img2 = Image.open(path +'1.png')
    img3 = Image.open(path +'2.png')
    img4 = Image.open(path +'3.png')
    
    img_rgb_1 = img1.convert('RGB')
    img_rgb_2 = img2.convert('RGB')
    img_rgb_3 = img3.convert('RGB')
    img_rgb_4 = img4.convert('RGB')
    
    img_main = img_rgb_1
    list_imgs = [img_rgb_2, img_rgb_3, img_rgb_4]

    filepath = path+'.pdf'
    
    img_main.save(filepath, save_all=True, append_images=list_imgs)
     
    for i in range(0,4):
        p = path + str(i) +'.png'
        
        try:
            os.remove(p)
        except OSError as e:
            print("Error: %s : %s" % (p, e.strerror)) 

    print("EDITPNG END")

    return filepath

def download(path):
    # with zipfile.ZipFile(path + 'Data.zip', 'w') as zip_file:
    #     for file in os.listdir(path):
    #         if file.endswith('.pdf'):
    #             zip_file.write(os.path.join(path, file), compress_type=zipfile.ZIP_DEFLATED)
    #     zip_file.close()
    if os.path.exists(path):
        binary_file = open(path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=a.pdf'
        return response
    else:
        print(path)
        print("can't download")
        return 0

def craw(url):

    headers = [
    {'User-Agent' : ''},
    ]

    page = requests.get(url, headers=headers[0])
    soup = bs(page.text, 'html.parser')
    
    result = []

    if url[8:22] == 'www.instiz.net':
        elements = soup.select("td.comment_memo")

        for element in elements:
            writer = element.find('span', {'class': 'href'}).find('a').text
            date = element.find('span', {'class': 'minitext'})['onmouseover']
            comment = element.find('div', {'class': 'comment_line'}).text

            data = {'link' : url,
                    'user_id' : writer,
                    'date' : re.sub("'", '', date[14:32]),
                    'comment' : comment
                    }
            result.append(data)

    elif url[8:23] == 'www.fmkorea.com':
        elements = soup.select("ul.fdb_lst_ul > li")

        for element in elements:
            writer = element.find('div', {'class': 'meta'}).find('a', {'href': '#popup_menu_area'}).text
            date = element.find('div', {'class': 'meta'}).find('span', {'class': 'date'}).text
            comment = element.find('div', {'class': 'comment-content'}).find('div').text
            
            data = {'link' : url,
                    'user_id' : writer,
                    'date' : date,
                    'comment' : comment
                    }
            result.append(data)
    return result    

