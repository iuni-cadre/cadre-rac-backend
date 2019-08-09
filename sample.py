import os
import docker
import sys
import boto3
from shutil import copyfile
import ntpath

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
cadre_rac = os.path.dirname(middleware)
util = cadre_rac + '/util'
sys.path.append(cadre_rac)

import util.config_reader

def run_docker_script(input_file_list, output_file_list):
    client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

    # We are building the docker image from the dockerfile here
    image = client.images.build(path='%s' % util.config_reader.get_docker_path(), tag='sample_test', forcerm=True)
    print(os.getcwd())
    print("The image has been built successfully. ")
    # Create a container and run a command in the container
    print(input_file_list)
    inputString = ",".join(input_file_list)
    print(inputString)

    shared_volume = '/home/aditya/user_package_run_dir'

    print(output_file_list)
    outputString = ",".join(output_file_list)
    print(outputString)
    command_list = ["python3", "script1.py"]
    for inputFile in input_file_list:
        file_name = ntpath.basename(inputFile)
        file_name_for_image = shared_volume + '/' + file_name
        copyfile(inputFile, file_name_for_image)
        command_list.append(file_name_for_image)

    print(command_list)

    container = client.containers.run('sample_test',
                                      detach=True,
                                      volumes={shared_volume: {'bind':'/home/aditya/user_package_run_dir', 'mode':'rw'}},
                                      command=command_list,
                                      remove=True)
    
    print(container.logs())
    print('The output of the file has been copied successfully outside the docker container')

    # Delete the docker container
    # client.containers.remove('sample_test', force=True)
    print('The container has been removed successfully.')

    # Delete the docker image
    client.images.remove('sample_test', force=True)
    print('The image has been removed successfully.')

    # Deleting the unused images
    # args = {"dangling": True}
    client.images.prune()

    # username = 'guptaadi'
    s3_job_dir = 'cpelikan/'
    s3_client = boto3.resource('s3',
                               aws_access_key_id=util.config_reader.get_aws_access_key(),
                               aws_secret_access_key=util.config_reader.get_aws_secret_access_key(),
                               region_name=util.config_reader.get_aws_region())
    root_bucket_name = util.config_reader.get_aws_s3_root()
    print(root_bucket_name)
    root_bucket = s3_client.Bucket(root_bucket_name)
    bucket_job_id = root_bucket_name + '/' + s3_job_dir
    print("Bucket Job ID: " + bucket_job_id)
    s3_location = 's3://' + bucket_job_id
    print(s3_location)
    i = 0
    for files in output_file_list:
        s3_client.meta.client.upload_file('/home/aditya/user_package_run_dir/%s' % output_file_list[i], root_bucket_name, 'cpelikan/tools/' + '%s' % output_file_list[i])
        i = i + 1
    

if __name__== "__main__":
    inputFileList = sys.argv[1].strip().split(',')
    outputFileList = sys.argv[2].strip().split(',')
    # userName = sys.argv[3]
    run_docker_script(inputFileList, outputFileList)
