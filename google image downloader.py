# https://www.youtube.com/watch?v=em96Ntm1DvU&ab_channel=PythonToday
# pip install icrawler

from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
    filters = dict(
        type='photo',
        #color='blackandwhite',
        size='large',
        #license='noncommercial, commercial',
        #date=((2020, 1, 1), (2022, 1, 1))
    )
    crawler = GoogleImageCrawler(storage={'root_dir': 'd:/img/Yellow Car'})
    #crawler.crawl(keyword='mr.robot', max_num=5)
    #crawler.crawl(keyword='mr.robot', max_num=5, min_size=(1000,1000), overwrite=True)
    crawler.crawl(
        keyword='Elegance Car',
        max_num=5,
        min_size=(2400, 2400),
        overwrite=True,
        filters=filters,
        file_idx_offset='auto'
    )

def main():
    google_img_downloader()

if __name__=='__main__':
    main()

