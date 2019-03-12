#  _*_ coding:utf-8 _*_
#  QQ: 2457179751
__author__ = 'xmduke'
from urllib import request
from bs4 import BeautifulSoup
import os,sys



base_url = "http://www.allitebooks.com/"
urls = [base_url]
for i in range(2,10):
    urls.append(base_url + 'page/%d' % i)

# 电子书列表
book_list = []


#获取网页源代码
def get_content(url):
    html = request.urlopen(url)
    content = html.read().decode('utf-8')
    return content


#控制url数量，避免电子书下载过多导致空间不够
#本例子下载前3页的电子书
#读者可以通过控制url[:3]中的数字，读取自己想要的的网页书

for url in urls[:1]:
    try:
        #获取每一页的链接
        content = get_content(url)
        soup = BeautifulSoup(content,'lxml')
        #print(soup)
        book_links = soup.find_all('div',class_="entry-thumbnail hover-thumb")
        book_links = [item('a')[0]['href'] for item in book_links]
        #print(book_links)
        print('\n获取第 %d 页 successfully!' % (urls.index(url) + 1))
    except Exception:
        #pass
        book_links = []
        print('\n 获取第 %d 页 failed!' % (urls.index(url) + 1))


    #如果每一页的链接获取成功
    if len(book_links):
        for book_link in book_links:
            #下载每一页中的电子书
            try:
                content = get_content(book_link)
                soup = BeautifulSoup(content,'lxml')
                #link = soup.find_all('span',class_="download-links")
                '''
              print (Soup.select('tr a')[0]) #取第一条a
              print (Soup.select('tr a')[0].attrs) #取a中的标签
              print (Soup.select('tr a')[0].string) #取a中的值（string）

              '''
                link = soup.select("span.download-links a")[0].attrs
                # link 输出结果例如: {'href': 'http://file.allitebooks.com/20190301/Search Engine Optimization Bible, 2nd Edition.pdf', 'target': '_blank'} 字典形式存在
                #print(link)
                book_url = link['href']
                #print(book_url)

                # 如果点自己书下载链接成功
                if book_url:
                    # 获取电子书名
                    book_name = book_url.split('/')[-1]
                    print('电子书名： %s' % book_name)
                    book_list.append(book_url)

            except Exception:
                print('获取第 %d 页中的第 %d 电子书失败' % ( urls.index(url)+1 , book_links.index(book_link)+1 ) )




# 本地下载电子书文件夹
local_ebook = os.path.join(os.path.curdir,'Ebooks')

if not os.path.exists(local_ebook):
    os.mkdir(local_ebook)
else:
    pass

with open(local_ebook + '\\ebooks.txt','w') as f:
    for item in book_list:
        f.write(str(item) + '\n')

print('写入txt文件完毕！')
