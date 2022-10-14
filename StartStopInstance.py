import boto3

# region EC2 instances are in
region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)


tagname = "Name"
tagvalue = "notJenkins"

instances=ec2.instances.filter(Filters=[
    {'Name':'tag:Name','Values': ['notJenkins']}
])

for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
    except:
        print(f'Error stopping {instance}')
