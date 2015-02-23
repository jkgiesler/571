from twython import TwythonStreamer
from datetime import datetime

'''
a much simpler interface for searching the twitter stream based on a query (labeled as track = )
note here that a comma represents OR if I were to use a space to seperate hashtags it would be considerd and AND
'''
class TweetStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data and data['coordinates'] is not None:
            
            raw_chi = open("chicago_raw.txt",'at')
            text = str(data['text'].encode('utf-8'))
            print(str(datetime.now()), file = raw_chi)
            print(text,file = raw_chi)
            raw_chi.close()
            

            #for the other project looking into violence
            interested = ["#guns","#ammo",'#shooting','#firearms','#bullets','#gun',\
               '#gunsale','#gunsforsale','#killa','#crime','#gunbroker','#guntrader','guns','violence',\
               'shooting','gang','firearm','gunsale','gun','gunsforsale','crime','bullets','Vicelord']


            for i in interested:
                if text.find(i) != -1 and text.find('gunna') == -1:
                    longitude = data['coordinates']['coordinates'][0]
                    latitude = data['coordinates']['coordinates'][1]
                    geo_search = gd.search((latitude,longitude))
                    outfile = open("chicago.txt","at")
                    print(str(datetime.now()), file = outfile)
                    print(data['coordinates']['coordinates'],file= outfile)
                    print(geo_search,file = outfile)
                    print(data['text'].encode('utf-8'), file = outfile)
                    outfile.close()
                    print(data['coordinates']['coordinates'])
                    print(geo_search)

                    print('\a')
                    break
			
    def on_error(self,status_code,data):
        print(status_code)
        self.disconnect

APP_KEY =  #NOTE TO SELF: THESE KEYS ARE PRIVATE. DO NOT BE AN IDIOT AND POST THIS CODE ON GITHUB
APP_SECRET = 
TWITTER_ACCESS_TOKEN = 
TWITTER_ACCESS_TOKEN_SECRET = 

streamer = TweetStreamer(APP_KEY,APP_SECRET,
	TWITTER_ACCESS_TOKEN,
	TWITTER_ACCESS_TOKEN_SECRET)

streamer.statuses.filter(locations='-93.184246,36.524706,-87.075848,42.929937')
