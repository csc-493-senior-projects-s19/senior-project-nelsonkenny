from app.config.loadConfig import *
from peewee import *
import os

def getDB ():
  config_abs_path = getAbsolutePath('app/config','config.yaml')
  cfg             = load_config(config_abs_path)
  db_name    = cfg['db']['db_name']
  host       = cfg['db']['host']
  username   = cfg['db']['username']
  password   = cfg['db']['password']
  DB         = MySQLDatabase ( db_name, host = host, user = username, passwd = password)
  return DB

DB = getDB()
class baseModel(Model):
  class Meta:
    database = DB
    
