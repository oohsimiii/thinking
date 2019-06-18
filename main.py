import webapp2
import os
import jinja2
from google.appengine.api import users
#from charity_models import Charities

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/")
        start_template = jinja_env.get_template("templates/LoginHandler.html")
        self.response.write(start_template.render())
        self.response.write('<a href= "' +
         login_url +'">Login with Gmail.</a>')
        user = users.get_current_user()
        if user:
            self.redirect("/loggedin")


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect("/nouser")
        else:
            email = user.nickname()
            logout_url = users.create_logout_url("/")
            dd = {"Logout": logout_url, "username": email}
            main_template = jinja_env.get_template("templates/MainHandler.html")
            self.response.write(main_template.render(dd))


class nouserHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect("/")
        else:
            self.redirect("/loggedin")


class charityAmountHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect("/nouser")
        else:
            Amount_template = jinja_env.get_template("templates/charityAmountHandler.html")
            self.response.write(Amount_template.render())


class LeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        leaderboard_template = jinja_env.get_template("templates/LeaderboardHandler.html")
        self.response.write(leaderboard_template.render())

class PersonalHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            personal_template = jinja_env.get_template("templates/PersonalHandler.html")
            self.response.write(personal_template.render())
        else:
            self.redirect("/nouser")

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/loggedin', MainHandler),
    ('/nouser', nouserHandler),
    ('/charityamount', charityAmountHandler),
    ('/Leaderboard', LeaderboardHandler),
    ('/personal', PersonalHandler)
], debug=True)
