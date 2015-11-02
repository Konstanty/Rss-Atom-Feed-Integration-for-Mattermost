#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elpatron@mailbox.org'

try:
    import html2text
except ImportError as exc:
    raise ImportError('Error: failed to import module ({}). Install missing modules using '
                      '"sudo pip install -r requirements.txt"'.format(exc))
    sys.exit(0)


class RssFeed:
    def __init__(self, name, url, user, channel, showname, showtitle, showdescription, showurl):
        self.Name = name
        self.Url = url
        self.User = user
        self.Channel = channel
        self.ShowName = showname
        self.ShowTitle = showtitle
        self.ShowDescription = showdescription
        self.ShowUrl = showurl
        self.LastTitle = ''
        self.NewTitle = ''
        self.ArticleUrl = ''
        self.Description = ''

    def jointext(self):
        text = ''
        h = html2text.HTML2Text()
        h.ignore_links = True
        self.Description = h.handle(self.Description)
        if self.ShowName == True:
            text += self.Name + '\n'
        if self.ShowTitle == True:
            text += self.NewTitle + '\n'
        if self.ShowDescription == True:
            text += self.Description + '\n'
        if self.ShowUrl == True:
            text += self.ArticleUrl
        return text
