from mongoengine import *
import logging

class Track(Document):
    URL = StringField(max_length=120, required=True)
    Track_date = DateTimeField()

    @property
    def my_time(self):
    	return self.Track_date.strftime('%Y-%m-%d')

    #PageCount = Track.objects.count()   #aggregation? 
    #print PageCount

    #for rows in Track.objects:
    #print rows.URL
    
	#Track1 = Track(text,now.strftime("%Y-%m-%d %H:%M"))
