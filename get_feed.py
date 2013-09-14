from TwitterAPI import TwitterAPI

consumer_key = 'e3xIgxEQmn3knlbpqEThxw'
consumer_secret = 'KIoFyRhaVRlBOBEsyNDyHg1pSWVC62ADjUpAhyo0kgc'
access_token_key = '1049595348-5rkCP0p2XqiLAGW3VzotzIsDjIuesPxV3DS2x5r'
access_token_secret = 'Xocm1c0cr7X9qnPEqxuhoHlheduiFVxpfsiy889QRg'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

num_result = 0
api.request('search/tweets', {'q':'zzz'})
iter = api.get_iterator()
for item in iter:
    print item

'''
api.request('statuses/filter', {'locations':'-74,40,-73,41'})
iter = api.get_iterator()
for item in iter:
    print item
    num_result += 1
    print num_result

    '''
