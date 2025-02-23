from pep_parse.constants import RESULTS_DIR

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [BOT_NAME + '.spiders']
NEWSPIDER_MODULE = BOT_NAME + '.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {BOT_NAME + '.pipelines.PepParsePipeline': 300}

FEEDS = {
    RESULTS_DIR + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
