import os
import docker

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
volumes= ['/home/chathuri/IUNI/cadre/rac/docker']
volume_bindings = {
                    '/home/chathuri/IUNI/cadre/rac/docker': {
                        'bind': '/shared',
                        'mode': 'rw',
                    },
}

image = client.images.build(path='/home/chathuri/IUNI/cadre/rac/cadre-rac-backend/myimages5', tag='sample_test1')
print(os.getcwd())
container = client.containers.run('sample_test1',
                                  detach=True,
                                  volumes={os.getcwd(): {'bind':'/tmp/', 'mode':'rw'}},
                                  command='python script.py /home/chathuri/IUNI/cadre/rac/cadre-rac-backend/myimages5/CadreQueryResult/guptaadi/ef28311e-aba1-4e82-badf-7761ad7c659d.csv')
print(container.logs())
