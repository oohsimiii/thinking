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
        dd = {"Login": login_url}
        start_template = jinja_env.get_template("templates/LoginHandler.html")
        self.response.write(start_template.render(dd))

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
            email = user.nickname()
            logout_url = users.create_logout_url("/")
            dd = {"Loginout": logout_url, "Loginoutresponse": "Logout", "username": email}
            Amount_template = jinja_env.get_template("templates/charityAmountHandler.html")
            self.response.write(Amount_template.render(dd))


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

class aboutHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email = user.nickname()
            logout_url = users.create_logout_url("/")
            dd = {"Loginout": logout_url, "Loginoutresponse": "Logout", "username": email}
            about_template = jinja_env.get_template("templates/aboutHandler.html")
            self.response.write(about_template.render(dd))
        else:
            email = "Main Page"
            login_url = users.create_login_url("/")
            dd = {"Loginout": login_url, "Loginoutresponse": "Login", "username": email}
            about_template = jinja_env.get_template("templates/aboutHandler.html")
            self.response.write(about_template.render(dd))



app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/loggedin', MainHandler),
    ('/nouser', nouserHandler),
    ('/charityamount', charityAmountHandler),
    ('/Leaderboard', LeaderboardHandler),
    ('/personal', PersonalHandler),
    ('/about', aboutHandler)
], debug=True)
