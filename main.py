from src.TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.TextSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.TextSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.TextSummarizer.logging import logger

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} started")
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} started")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} started")
    model_trainer_pipeline=ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

