#
##
### John Farrell
#### NYU ITP
##### Adapted from Gilad Lotan / Social Data Analysis

from urlparse import urlparse
from instagram.client import InstagramAPI
import pickle

# Fill in your API information
client_id = 'YOUR_ID'
client_secret = 'YOUR_SECRET'
api = InstagramAPI(client_id=client_id, client_secret=client_secret)


# Do your first hashtag search
used_tag='YOUR_HASHTAG'
max_tag_id = 0
all_media = []
ans = api.tag_recent_media(33,max_tag_id,used_tag)

# Get your first media items and max_tag_id from that search
for m in ans[0]:
	all_media.append(m)
	parsed = urlparse(ans[1])
	params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

# Iterate backwards through media, using max_tag_id, appending posts to the all_media array
for i in range(1000):
	try:
	    max_tag_id = int(params['max_tag_id'])
	    ans = api.tag_recent_media(33,max_tag_id-1, used_tag)
	    for m in ans[0]:
	        all_media.append(m)
	        
	    parsed = urlparse(ans[1])
	    params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}
	except AttributeError:
		break

# Save a pickle file to work off in the future
pickle.dump(all_media, open('%s_data.p'%used_tag, 'wb'))