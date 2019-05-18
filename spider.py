from urllib.request import urlopen # a module used to connect to webpages
from link_finder import LinkFinder
from domain import *
from general import *

class Spider:

    project_name = '' # name of the project
    base_url = '' # usualy the home page
    domain_name = '' # ensure to connect to the valid domain name
    queue_file = '' # location of the queue file
    crawled_file = '' # location of the crawled file
    queue = set() # create empty set to save links in queue
    crawled = set() # create empty set to save crawled links
    