import os 
import time


class FileCrawler:
    
    def __init__(self, path=os.curdir):
        self.path = path
    
    def run(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return os.listdir(self.path)

    def get_modify_date(self, file_list):
        """[summary]
        """
        for file in file_list:

            mod_epoc_time = os.path.getmtime(file)

            raw_time = os.path.getmtime(file)
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_epoc_time))
            
            print(f'{file} modified on: {formatted_time}')

crawler = FileCrawler()

print(crawler.run())
crawler.get_modify_date(crawler.run())
