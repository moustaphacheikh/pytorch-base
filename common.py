
#==================================================
# Defines useful constructs used during training
# and evaluation of multiple models
#==================================================

from models import *

VALID_MODEL_NAMES = {
        'model' : (model.add_model_options, model.validate_model_options, model.Model)
        }

def get_model(name):
    try:
        return VALID_MODEL_NAMES[name]
    except:
        raise KeyError('Model is not supported, did you forget to add it to the VALID_MODEL_NAMES dict?')

