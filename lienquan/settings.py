BOT_NAME = "lienquan"

SPIDER_MODULES = ["lienquan.spiders"]
NEWSPIDER_MODULE = "lienquan.spiders"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 32

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

ITEM_PIPELINES = {
    'lienquan.pipelines.SQLitePipeline': 1
}

USER_AGENT = """
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
"""
