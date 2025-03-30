import os
from box.exceptions import BoxValueError
import yaml
from cnnclassifer import logger
import json
import joblib
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> config_box:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return config_box(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for  path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created Dir at :{path}")

@ensure_annotations
def save_json(path:Path,data: dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"Json file saved at:{path}")

@ensure_annotations
def load_json(path: Path) ->config_box:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"json file load at : {path}")
    return config_box(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    l=joblib.dump(value=data,filename=path)
    logger.info(f"binary file is saved at :{path}")

#@ensure_annotations
def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb')as f:
        f.write(imgdata)
        f.close()

#@ensure_annotations
def encodeImageintoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())    
