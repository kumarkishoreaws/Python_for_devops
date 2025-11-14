import boto3

client = boto3.client('s3')

response = client.list_objects(
Bucket='etomosphere-test-s3'
) 

key = response["Contents"][1]["Key"]
print(key)