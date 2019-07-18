import os
import docker

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
volumes= ['/home/aditya/Documents/docker']
volume_bindings = {
                    '/home/aditya/Documents/docker': {
                        'bind': '/shared',
                        'mode': 'rw',
                    },
}

# We are building the docker image from the dockerfile here
image = client.images.build(path='/home/aditya/Documents/myimages5/', tag='sample_test', forcerm=True)
print(os.getcwd())
print("The image has been built successfully. ")
# Create a container and run a command in the container
container = client.containers.run('sample_test',
                                  detach=True,
                                  volumes={os.getcwd(): {'bind':'/tmp/', 'mode':'rw'}},
                                  command='python script.py /home/aditya/Documents/myimages5/CadreQueryResult/guptaadi/ef28311e-aba1-4e82-badf-7761ad7c659d.csv',
                                  remove=True)
print(container.logs())
print('The output of the file has been copied successfully outside the docker container')

# Delete the docker container
print('The container has been removed successfully.')

# Delete the docker image
client.images.remove('sample_test', force=True)
print('The image has been removed successfully.')

# Deleting the unused images
client.images.prune()
