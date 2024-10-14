import requests
import bs4
import os
urls = ['https://tangcuxiaojikuai.xyz/archives/', 'https://tangcuxiaojikuai.xyz/archives/page/2', 'https://tangcuxiaojikuai.xyz/archives/page/3', 'https://tangcuxiaojikuai.xyz/archives/page/4', 'https://tangcuxiaojikuai.xyz/archives/page/5', 'https://tangcuxiaojikuai.xyz/archives/page/6', 'https://tangcuxiaojikuai.xyz/archives/page/7', 'https://tangcuxiaojikuai.xyz/archives/page/8', 'https://tangcuxiaojikuai.xyz/archives/page/9', 'https://tangcuxiaojikuai.xyz/archives/page/10']
blog_urls=[]
blognames=[]
filename='糖醋小鸡块blog'
if not os.path.exists(filename):
    os.mkdir(filename)
for url in urls: 
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content,'html.parser')
    element = soup.find_all('a',{'class':'my-post-title-link'})
    hrefs = [link.get('href') for link in element]
    blog_urls.extend(hrefs)
    blogname = soup.find_all('span', {'itemprop': 'name'})
    blognames.extend([name.text for name in blogname])

for i,blog_url in enumerate(blog_urls):
    blog_url = 'https://tangcuxiaojikuai.xyz'+blog_url
    response = requests.get(blog_url)
    if response.status_code != 200:
        print('Error:', response.status_code)
        continue
    soup = bs4.BeautifulSoup(response.content,'html.parser')
    html_str=str(soup)
    if '/' in blognames[i] :
        blognames[i] = blognames[i].replace('/','-')
    if "\"" in blognames[i] :
        blognames[i] = blognames[i].replace("\"","")
    filename = '糖醋小鸡块blog/' + blognames[i] + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_str)
