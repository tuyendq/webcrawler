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

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name # set the value for the clase variable so that all spiders have the same information
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt' # define path of queue file
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot() # the method creating project directory and data files
        self.crawl_page('First spicder', Spider.base_url) # method starting the page crawling and print message to user
        
    @staticmethod # define the method as static
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_file:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_file()