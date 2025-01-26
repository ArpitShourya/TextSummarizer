import os,sys,logging

lod_dir="logs"
log_filepath=os.path.join(lod_dir,"continuous_logs.log")
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"
os.makedirs(lod_dir,exist_ok=True)
logging.basicConfig(level=logging.INFO,
                    format=logging_str,
                    handlers=[
                        logging.FileHandler(log_filepath),
                        logging.StreamHandler(sys.stdout)
                    ]
                )
logger=logging.getLogger("summarizerlogger")