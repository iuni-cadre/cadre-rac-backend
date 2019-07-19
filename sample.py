import os
import docker
import sys

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
cadre_rac = os.path.dirname(middleware)
util = cadre_rac + '/util'
sys.path.append(cadre_rac)

import util.config_reader

def functionToRunScriptOnDocker(filepath):
    client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

    # We are building the docker image from the dockerfile here
    image = client.images.build(path='%s' % util.config_reader.get_docker_path(), tag='sample_test', forcerm=True)
    print(os.getcwd())
    print("The image has been built successfully. ")
    # Create a container and run a command in the container
    container = client.containers.run('sample_test',
                                    detach=True,
                                    volumes={os.getcwd(): {'bind':'/tmp/', 'mode':'rw'}},
                                    command='python script.py %s' % filepath,
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


if __name__== "__main__":
    functionToRunScriptOnDocker(sys.argv[1])
