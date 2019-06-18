from google.appengine.ext import ndb

class Charities(ndb.Model):
    charity_name = ndb.StringProperty(required=True)
    cause = ndd.StringProperty(required = True)

class Username(ndb.Model):
    username_id = ndb.IntegerProperty(required = True)
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)

class Donation(ndb.Model):
    amount = ndb.IntegerProperty(required=True)
    
