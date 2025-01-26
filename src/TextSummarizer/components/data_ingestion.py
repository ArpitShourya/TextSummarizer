import os, zipfile
import urllib.request as request
from src.TextSummarizer.logging import logger
from src.TextSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info("Dataset Downloaded")

        else:
            logger.info("File already exist")
        
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)