import logging
import os, traceback, sys
import configparser

abspath = os.path.abspath(os.path.dirname(__file__))
parent = os.path.dirname(abspath)
sys.path.append(parent)

logger = logging.getLogger(__name__)


def get_cadre_rac_config():
    try:
        config_path = parent + '/conf/cadre_rac.config'
        if os.path.isfile(config_path):
            config = configparser.RawConfigParser()
            config.read(config_path)
            return config
        else:
            logger.error('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
            raise Exception('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')


def get_docker_path():
    try:
        config = get_cadre_rac_config()
        docker_path = config['RAC_BACKEND']['docker_path']
        return docker_path
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
        raise Exception('Unable to find cadre_rac.config file !')

def get_aws_access_key():
    try:
        config = get_cadre_rac_config()
        access_key = config['AWS']['aws_access_key_id']
        return access_key
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
        raise Exception('Unable to find cadre_rac.config file !')


def get_aws_secret_access_key():
    try:
        config = get_cadre_rac_config()
        access_key_secret = config['AWS']['aws_secret_access_key']
        return access_key_secret
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
        raise Exception('Unable to find cadre_rac.config file !')


def get_aws_region():
    try:
        config = get_cadre_rac_config()
        region_name = config['AWS']['region_name']
        return region_name
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
        raise Exception('Unable to find cadre_rac.config file !')


def get_aws_s3_root():
    try:
        config = get_cadre_rac_config()
        s3_root = config['AWS']['s3_root_dir']
        return s3_root
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find cadre_rac.config file. Make sure you have cadre_rac.config inside conf directory !')
        raise Exception('Unable to find cadre_rac.config file !')

