import os
import zipfile
import gdown  
from Cnnclassifier import logger
from Cnnclassifier.utils.common import get_size
from Cnnclassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    def download_file(self):
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file

            os.makedirs(self.config.root_dir, exist_ok=True)

            logger.info(f"Downloading data from {dataset_url}")

            file_id = dataset_url.split("/")[-2]

            prefix = "https://drive.google.com/uc?export=download&id="

            gdown.download(
                prefix + file_id,
                str(zip_download_dir),
                quiet=False
            )

            logger.info("Download completed successfully!")

        except Exception as e:
            raise e
    

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
    
    # Remove unwanted classes
        import shutil

        dataset_path = os.path.join(unzip_path,
           "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone"
        )

        for folder in ["Cyst", "Stone"]:
            folder_path = os.path.join(dataset_path, folder)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                print(f"Deleted: {folder_path}")     

    logger.info("Extraction completed.")