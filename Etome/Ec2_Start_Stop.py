import boto3 

ec2 = boto3.client('ec2')

#Function to get all instances
def get_dev_instances():
    response = ec2.describe_instances(
        Filters = [
            {"Name" : "tag:Environment" , "Values" :["TESTING_SERVER"]}
        ] 
    )
    instance_Ids = []
    for reservation in response["Reservations"]:
      for instance in reservation["Instances"]:
        instance_Ids.append(instance["InstanceId"])
    return instance_Ids

# Function to Stop instances
def stop_dev_instances():
    ids = get_dev_instances()

    if ids:
        ec2.stop_instances(InstanceIds = ids)
        print("Stopped instances -", ids)
    else:
        Print("No Instances are there to stop.")


# Function to start instnaces
def start_dev_instances(): 
  ids = get_dev_instances()

  if ids:
     ec2.start_instances(InstanceIds = ids)
     print("Started Instances -" , ids)
  else:
     print("There is no instances to start")

stop_dev_instances()
start_dev_instances()