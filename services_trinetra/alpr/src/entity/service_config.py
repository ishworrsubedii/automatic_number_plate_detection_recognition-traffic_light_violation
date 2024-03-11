from pydantic import BaseModel


class DetectionConfig(BaseModel):
    model_path: str


class RecognitionConfig(BaseModel):
    det_model: str
    recognition_model: str
    rec_char_dict: str


class EmbossedNumberPlateConfig(BaseModel):
    det_model: str
    recognition_model: str
    cls_model_dir: str
    char_dict: str
