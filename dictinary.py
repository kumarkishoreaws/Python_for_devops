ec2_instances_info = [
   {
    "name" :"instance-001",
    "type"  : "t2.micro",
    "region": "us-west-1",
    "status": "running"
    },

    {
    "name" :"instance-002",
    "type" : "t2.medium",
    "region": "us-east-1",
    "status": "stopped"
    },

    {
    "name" :"instance-003",
    "type" : "t2.large",
    "region": "eu-central-1",
    "status": "running"
    }

]

print(ec2_instances_info[1]["name"] ,ec2_instances_info[1]["status"])