import boto3

client = boto3.client('s3')

response = client.list_objects(
Bucket='etomosphere-s3'
) 

key = response["Contents"][0]["Key"]
print(key)