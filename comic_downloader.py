

import requests
import os 
import bs4
# select The url
url='http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
#last url will be ended by #
while not url.endswith('#'):
	#read the html page
	res=requests.get(url)
	soup=bs4.BeautifulSoup(res.text)
	# comic images lies in div tag with id=comic inside image tag
	comic=soup.select('#comic img')
	#link dont have the protocol to fetch data
	comic_url='http:'+comic[0].get('src')
	print('downloading' + comic_url)
	comic_img=requests.get(comic_url)
	print('downloaded')
	#creating file to store image locally
	comic_file=open(os.path.join('xkcd',os.path.basename(comic_url)),'wb')
	for chunk in comic_img.iter_content(100000):
		comic_file.write(chunk)
	comic_file.close()
	#prev link redirect to previous image
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')


