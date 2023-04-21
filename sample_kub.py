import base64
import os
import docker
import sys
import boto3
import string
import random
from shutil import copyfile
import ntpath
from kubernetes import client, config, utils
from kubernetes.stream import stream
import kubernetes.client
from kubernetes.client.rest import ApiException

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
cadre_rac = os.path.dirname(middleware)
util = cadre_rac + '/util'
sys.path.append(cadre_rac)

import util.config_reader

config.load_kube_config()
configuration = kubernetes.client.Configuration()
api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))


def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def kube_create_job_object(name,
                           container_image,
<<<<<<< HEAD
                           namespace="jhub",
=======
                           namespace="default",
>>>>>>> 3fc69a286494991bbdaa5c658a77e0fade2e9756
                           container_name="jobcontainer",
                           env_vars={},
                           input_file_list={},
                           output_file_list={}):
    """
    Create a k8 Job Object
    Minimum definition of a job object:
    {'api_version': None, - Str
    'kind': None,     - Str
    'metadata': None, - Metada Object
    'spec': None,     -V1JobSpec
    'status': None}   - V1Job Status
    Docs: https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Job.md
    Docs2: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#writing-a-job-spec
    Also docs are pretty pretty bad. Best way is to ´pip install kubernetes´ and go via the autogenerated code
    And figure out the chain of objects that you need to hold a final valid object So for a job object you need:
    V1Job -> V1ObjectMeta
          -> V1JobStatus
          -> V1JobSpec -> V1PodTemplate -> V1PodTemplateSpec -> V1Container

    Now the tricky part, is that V1Job.spec needs a .template, but not a PodTemplateSpec, as such
    you need to build a PodTemplate, add a template field (template.template) and make sure
    template.template.spec is now the PodSpec.
    Then, the V1Job.spec needs to be a JobSpec which has a template the template.template field of the PodTemplate.
    Failure to do so will trigger an API error.
    Also Containers must be a list!
    Docs3: https://github.com/kubernetes-client/python/issues/589
    """
    # Body is the object Body
    body = client.V1Job(api_version="batch/v1", kind="Job")
    # Body needs Metadata
    # Attention: Each JOB must have a different name!
    body.metadata = client.V1ObjectMeta(namespace=namespace, name=name)
    # And a Status
    body.status = client.V1JobStatus()
    # Now we start with the Template...
    template = client.V1PodTemplate()
    template.template = client.V1PodTemplateSpec()
    # Passing Arguments in Env:
    env_list = []
    for env_name, env_value in env_vars.items():
        env_list.append(client.V1EnvVar(name=env_name, value=env_value))

<<<<<<< HEAD
    shared_volume = '/home/ubuntu/efs/home/cadre-query-results/chathuri'
=======
    shared_volume = '/home/chathuri/mounts'
>>>>>>> 3fc69a286494991bbdaa5c658a77e0fade2e9756
    shared_volume_in_pod = '/data'
    # input_dir = shared_volume + '/input'
    # if not os.path.exists(input_dir):
    #     os.makedirs(input_dir)
    #
    # output_dir = shared_volume + '/output1'
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    print(output_file_list)
    outputString = ",".join(output_file_list)
    print(outputString)

    command_list = ["python", "helloworld.py"]
    shared_inputs = []
    for inputFile in input_file_list:
        file_name = ntpath.basename(inputFile)
        file_name_for_image = shared_volume + '/' + file_name
        copyfile(inputFile, file_name_for_image)
        shared_inputs.append(shared_volume_in_pod + '/' + file_name)
    shared_inputs_as_string = ",".join(shared_inputs)
    output_names = ",".join(output_file_list)
    args = [shared_inputs_as_string, output_names, shared_volume_in_pod]
    # args.append(shared_inputs_as_string)
    # args.append(output_names)
    # args.append(shared_volume)
    print(args)

    pod = client.V1Pod()
    pod.metadata = client.V1ObjectMeta(name="line-count")
    hostpathvolumesource = client.V1HostPathVolumeSource(path=shared_volume, type='DirectoryOrCreate')
<<<<<<< HEAD
    volume_spec = client.V1PersistentVolumeSpec(storage_class_name='', volume_mode='Filesystem', access_modes=['ReadWriteMany'], host_path=hostpathvolumesource, capacity={'storage': '2Gi'})
    pv_meta = client.V1ObjectMeta(name='cadre-query-results')
    persistent_volume = client.V1PersistentVolume(metadata=pv_meta, api_version='v1', kind='PersistentVolume', spec=volume_spec)
    resource_requirements = client.V1ResourceRequirements(limits={'cpu': 2, 'memory': '80Mi', 'storage': '2Gi'}, requests={'cpu': 1, 'memory': '40Mi','storage': '1Gi'})
    claim_spec = client.V1PersistentVolumeClaimSpec(storage_class_name='', access_modes=['ReadWriteMany'], resources=resource_requirements)
    pvc_meta = client.V1ObjectMeta(name='efs')
    persistent_volume_claim = client.V1PersistentVolumeClaim(api_version='v1', metadata=pvc_meta, kind='PersistentVolumeClaim', spec=claim_spec)
    claim_volume_source = client.V1PersistentVolumeClaimVolumeSource(claim_name='efs')
    volume_mounts = [client.V1VolumeMount(mount_path=shared_volume_in_pod, name='cadre-query-results',sub_path='home/cadre-query-results/chathuri')]
    #api_instance.create_persistent_volume(body=persistent_volume, pretty=True)
    #api_instance.create_namespaced_persistent_volume_claim(body=persistent_volume_claim, namespace='default', pretty=True)
=======
    volume_spec = client.V1PersistentVolumeSpec(storage_class_name='manual', volume_mode='Filesystem', access_modes=['ReadWriteMany'], host_path=hostpathvolumesource, capacity={'storage': '2Gi'})
    pv_meta = client.V1ObjectMeta(name='task-pv-volume')
    persistent_volume = client.V1PersistentVolume(metadata=pv_meta, api_version='v1', kind='PersistentVolume', spec=volume_spec)
    resource_requirements = client.V1ResourceRequirements(limits={'cpu': 2, 'memory': '80Mi', 'storage': '2Gi'}, requests={'cpu': 1, 'memory': '40Mi','storage': '1Gi'})
    claim_spec = client.V1PersistentVolumeClaimSpec(storage_class_name='manual', access_modes=['ReadWriteMany'], resources=resource_requirements)
    pvc_meta = client.V1ObjectMeta(name='task-pv-claim')
    persistent_volume_claim = client.V1PersistentVolumeClaim(api_version='v1', metadata=pvc_meta, kind='PersistentVolumeClaim', spec=claim_spec)
    claim_volume_source = client.V1PersistentVolumeClaimVolumeSource(claim_name='task-pv-claim')
    volume_mounts = [client.V1VolumeMount(mount_path=shared_volume_in_pod, name='task-pv-storage')]
    api_instance.create_persistent_volume(body=persistent_volume, pretty=True)
    api_instance.create_namespaced_persistent_volume_claim(body=persistent_volume_claim, namespace='default', pretty=True)
    # volume = client.V1Volume(name='test-volume', empty_dir={})
    # client.V1PersistentVolume()
    # volume_mount = client.V1VolumeMount(mount_path=shared_volume, name=volume.name)

    container = client.V1Container(name=container_name,
                                   image=container_image,
                                   env=env_list,
                                   command=command_list,
                                   args=args,
                                   image_pull_policy='Always')

    container.volume_mounts = volume_mounts
    spec = client.V1PodSpec(containers=[container], restart_policy='Never')
    volume = client.V1Volume(name='cadre-query-results', persistent_volume_claim=claim_volume_source)
    spec.volumes = [volume]
    # And finaly we can create our V1JobSpec!
    pod.spec = spec
    # body.spec = client.V1JobSpec(ttl_seconds_after_finished=600, template=template.template)
    return pod


def run_docker_script(input_file_list, output_file_list):
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    # We are building the docker image from the dockerfile here
    client.images.build(path='%s' % util.config_reader.get_docker_path(), tag='line_count')
    image = client.images.get('line_count')
    image.tag('chathuri/cadre-packages', tag='latest')
    auth_config_payload = {'username': 'chathuri', 'password': ''}
    for line in client.images.push('chathuri/cadre-packages', stream=True, decode=True, auth_config=auth_config_payload):
        print(line)
    # client.images.push('chathuri/cadre-packages', 'latest', stream=True, decode=True, auth_config=auth_config_payload)

    image_name = 'chathuri/cadre-packages'
    job_name = id_generator()

    body = kube_create_job_object(job_name, image_name, env_vars={"DOCKER_TLS_VERIFY": "1", "DOCKER_HOST":"tcp://192.168.99.100:2376", "DOCKER_CERT_PATH":"/home/chathuri/.minikube/certs"}, input_file_list=input_file_list, output_file_list=output_file_list)
    try:
        api_response = api_instance.create_namespaced_pod("default", body, pretty=True)
        exec_command = ['/bin/sh']
        # resp = stream(api_instance.connect_get_namespaced_pod_exec, 'line-count', 'default',
        #               command=exec_command,
        #               stderr=False, stdin=False,
        #               stdout=True, tty=False)
        #
        # file = open(input_file_list[0], "r")
        #
        # commands = []
        # commands.append("cat <<'EOF' >" + '/data/1.csv' + "\n")
        # commands.append(file.read())
        # commands.append("EOF\n")
        #
        # while resp.is_open():
        #     resp.update(timeout=1)
        #     if resp.peek_stdout():
        #         print("STDOUT: %s" % resp.read_stdout())
        #     if resp.peek_stderr():
        #         print("STDERR: %s" % resp.read_stderr())
        #
        #     if commands:
        #         c = commands.pop(0)
        #         resp.write_stdin(c)
        #     else:
        #         break
        #
        # resp.close()
        print(api_response)
    except ApiException as e:
        print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)


if __name__== "__main__":
    inputFileList = sys.argv[1].strip().split(',')
    outputFileList = sys.argv[2].strip().split(',')
    # package_id = sys.argv[3]
    # userName = sys.argv[3]
    run_docker_script(inputFileList, outputFileList)