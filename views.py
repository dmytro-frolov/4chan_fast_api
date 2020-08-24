import requests
import bs4
import lxml

from abc import abstractmethod, ABC
from collections import namedtuple


class IThread(ABC):
    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def to_json(self):
        pass

class Post:
    name = None
    date = None
    post_id = None
    picture = None
    text = None
    quote_link = None

    def __init__(self, html_obj):
        self.html_obj = html_obj

    def parse(self):
        self.text = self.html_obj.xpath('blockquote/text()')
        self.name = self.html_obj.xpath('*/span[@class="nameBlock"]/span/text()')[0]
        pass


class Thread(IThread):
    posts = None

    def __init__(self, html_obj):
        self.html_obj = html_obj
    
    def parse(self):
        posts = self.html_obj.xpath('*/div[contains(@class, "post ")]')

        for post in posts:
            p = Post(post)
            p.parse()
            print
            
        pass

    def to_json(self):
        pass


class Board(IThread):
    replies = 0
    date = None
    thread_id = None

    threads = None
    # def __init__(self, thread_id, date, replies):
    def __init__(self, html_obj):
        self.html_obj = html_obj

    def parse(self):
        self.threads = self._get_threads()
        self._get_thread_info()
        pass

    def to_json(self):
        return {}

    def _get_threads(self):
        thread_list = []
        threads = self.html_obj.xpath('//*[@class="thread"]')
        
        for thread in threads:
            t = Thread(thread)
            t.parse()

            thread_list.append(t)


        return thread_list

    
    def _get_thread_info(self):
        pass