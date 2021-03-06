'''This script loads the yaml file, which holds all configuration information not saved in the database.
'''
from app.logic.absolute_path import *
import yaml, os
import logging

def load_config(file):
    with open(file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg

def get_cfg():
    config_abs_path = getAbsolutePath('app/config','config.yaml')
    cfg             = load_config(config_abs_path)
    return cfg
    