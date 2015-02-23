from instagram.client import InstagramAPI
import requests
#http://nbviewer.ipython.org/github/katychuang/Pyladies-ImageAnalysis/blob/master/Instagram%20Image%20Analysis.ipynb


#private keys given by instagram
INSTAGRAM_CLIENT_ID = 
INSTAGRAM_CLIENT_SECRET = 

api = InstagramAPI(client_id = INSTAGRAM_CLIENT_ID, 
	client_secret = INSTAGRAM_CLIENT_SECRET)

popular_media = api.media_popular(count=20)

photolist = []
for media in popular_media:
    photolist.append(media.images['standard_resolution'].url)

counter = 1

#http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
for link in photolist:
	response = requests.get(link)
	if response.status_code ==200:
		f = open("image"+str(counter)+".jpg",'wb')
		f.write(response.content)
		f.close()
	counter += 1
