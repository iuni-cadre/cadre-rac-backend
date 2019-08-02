import os
import docker
import sys
import boto3

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
cadre_rac = os.path.dirname(middleware)
util = cadre_rac + '/util'
sys.path.append(cadre_rac)

import util.config_reader

def functionToRunScriptOnDocker(inputFileList, outputFileList):
    client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

    # We are building the docker image from the dockerfile here
    image = client.images.build(path='%s' % util.config_reader.get_docker_path(), tag='sample_test', forcerm=True)
    print(os.getcwd())
    print("The image has been built successfully. ")
    # Create a container and run a command in the container
    # print(inputFileList)
    inputString = ",".join(inputFileList)
    print(inputString)

    command_lst = ['python3', 'script1.py', inputFileList[0], inputFileList[1]]

    print(command_lst)
    container = client.containers.run('sample_test',
                                      detach=True,
                                      volumes={'/tmp/': {'bind':'/tmp/', 'mode':'rw'}},
                                      command=command_lst,
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

    username = 'guptaadi'
    s3_job_dir = username + '/'
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
    # for files in outputFileList:
    #     s3_client.meta.client.upload_file('/tmp/%s' % outputFileList[i], root_bucket_name, username + '/tools/' + '%s' % outputFileList[i])
    #     i = i + 1
    

if __name__== "__main__":
    inputFileList = sys.argv[1].strip().split(',')
    outputFileList = sys.argv[2].strip().split(',')
    functionToRunScriptOnDocker(inputFileList, outputFileList)
