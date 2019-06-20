from google.appengine.ext import ndb
import sys
sys.setrecursionlimit(2000)

class Charity(ndb.Model):
    charity_name = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required = True)

#class Username(ndb.Model):
    #username_id = ndb.IntegerProperty(required = True)
    #first_name = ndb.StringProperty(required = True)
    #last_name = ndb.StringProperty(required = True)

#class Donation(ndb.Model):
    #amount = ndb.IntegerProperty(required=True)
