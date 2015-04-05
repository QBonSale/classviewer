`scrapy crawl UCLA` to scrape, followed by `-o foo.json/csv/xml` for output, `-a refresh=1` to read all, default is 0

change the commented Request in `start_requests` to switch between one page mode or all.