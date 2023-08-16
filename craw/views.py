#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import CrawData
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import requests
from bs4 import BeautifulSoup as bs

import os
import re


os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django
django.setup()

from craw.models import CrawData

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def craw_list(request):
    input_url = request.GET.get('input_url')
    keyword = request.GET.get('keyword')
    craw_data_dict = craw(input_url)
    craw_list=[]
    for item in craw_data_dict:
        if keyword in item['comment']:
                craw_item=CrawData()

                craw_item.link=item['link']
                craw_item.user_id=item['user_id']
                craw_item.date=item['date']
                craw_item.comment = item['comment']
                
                craw_list.append(craw_item)

                context = {
                    'craw_item' : craw_item, 
                    'craw_list' : craw_list
                }

    return render(request, 'craw/craw_list.html', context)


# def craw_list(request):
#     craw_list = CrawData.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(craw_list, 10)

#     try:
#         page_obj = paginator.get_page(page)
#     except PageNotAnInteger:
#         page = 1
#         page_obj = paginator.page(page)
#     except EmptyPage:
#         page = paginator.num_pages
#         page_obj = paginator.page(page)


#     context = {'craw_list': craw_list, 'page_obj':page_obj, 'paginator':paginator}
#     return render(request, 'craw/craw_list.html', context)


def tractor_main(request):
    return render(request, 'craw/tractor_main.html')



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


# def catch(request):
#     input_url = request.GET.get('input_url')
#     keyword = request.GET.get('keyword')
#     craw_data_dict = craw(input_url)
#     craw_list=[]
#     for item in craw_data_dict:
#         if keyword in item['comment']:
#                 craw_item=CrawData()

#                 craw_item.link=item['link']
#                 craw_item.user_id=item['user_id']
#                 craw_item.date=item['date']
#                 craw_item.comment = item['comment']

#                 print(craw_item.comment)
                
#                 craw_list.append(craw)
#                 context = {
#                     # 'craw_item' : craw_item, 
#                     'craw_list' : craw_list
#                 }

#     return render(request, 'craw/craw_list.html', context)

