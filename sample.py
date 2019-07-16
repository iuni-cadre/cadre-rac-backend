import docker
import tarfile
import os
import requests
from docker import Client
from io import BytesIO

os.chdir(r"/home/aditya/Documents/myimages5")

#Create Tar file
tarFile = tarfile.open("Dockerfile.tar.gz", 'w:gz')

files = os.listdir(".")
for f in files:
    tarFile.add(f)

#List files in tar
for f in tarFile.getnames():
    print("Added %s" % f)

tarFile.close()

headers = {
    'Content-Type': 'application/tar',
}

params = (
    ('t', 'sample_test'),
)

data = open('Dockerfile.tar.gz', 'rb').read()
# We are building the docker image from the dockerfile here
try:
    response = requests.post('http://localhost:2375/build?t=sample_test', headers=headers, params=params, data=data)
except requests.exceptions.RequestException as e:
    print('Exception caught:', e)

# Create a container and run a command in the container
dockerClient = Client(base_url='http://localhost:2375')
container = dockerClient.create_container(image='sample_test', command='python script.py /home/aditya/Documents/myimages5/CadreQueryResult/guptaadi/ef28311e-aba1-4e82-badf-7761ad7c659d.csv')
response = dockerClient.start(container)
print(container)

# Copy the output of the python script
# dockerClient.copy('/usr/local/bin/output.txt', '~/output.txt') 

# raw_stream,status = dockerClient.get_archive(container, '/usr/local/bin')
# print(status)
# tar_archive = BytesIO(b"".join((i for i in raw_stream)))
# t = tarfile.open(mode='r:', fileobj=tar_archive)
# text_from_container_file = t.extractfile('output.txt').read().decode('utf-8')
print('The output of the file has been copied successfully outside the docker container')

# Delete the container
# dockerClient.remove_container(container, force = 'true')
print('The container has been removed successfully.')

# Delete the docker image
# dockerClient.remove_image('sample_test', force = 'true')
print('The image has been removed successfully.')
