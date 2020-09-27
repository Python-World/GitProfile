from lxml.html import fromstring
from datetime import datetime
from .Connect import Connect
import requests
import json


class GitUser(Connect):
    def __init__(self, user):
        self.user = Connect.conn.get_user(user)
        self.username = self.user.login
        self.profile = self.user.html_url
        self.picture = self.user.avatar_url
        self.name = self.user.name
        self.email = self.user.email
        self.followers = self.user.followers
        self.following = self.user.following
        self.repos = self.user.public_repos
        self.gist = self.user.public_gists
        self.bio = self.user.bio
        self.blog = self.user.blog
        self.created = self.__get_date(self.user.created_at)
        self.modified = self.__get_date(self.user.updated_at)

    def __get_date(self, date):
        return datetime.strftime(date, '%d-%b-%Y')

    def get_user(self):
        return self.__dict__

    def get_languages(self):
        language_contribution = {}
        try:
            req = requests.get(
                'https://github.com/search?q=user%3A{}'.format(self.username))
            response = fromstring(req.text,)
            languages = response.xpath('//a[contains(@href,"search?l=")]')
            for language in languages:
                lang = language.xpath('./text()')[-1].strip()
                total = language.xpath('./span/text()')[-1]
                language_contribution[lang] = total
        except Exception as ex:
            print(ex)
        return language_contribution

    def get_overview(self):
        overview = {}
        try:
            req = requests.get('https://github.com/{}'.format(self.username))
            response = fromstring(req.text,)
            details = response.xpath(
                '//*[@class="js-activity-overview-graph-container"]/@data-percentages')
            details = details[0] if details else '{}'
            overview = json.loads(details)
        except Exception as ex:
            print(ex)
        return overview
