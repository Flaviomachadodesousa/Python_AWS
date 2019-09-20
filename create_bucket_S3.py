import boto3

def Create_Bucket():
    # Bucket Name to Create
    bucket_name = input('Enter the name of the bucket you want to create. ' )

    # Calling the SDK Function
    s3 = boto3.resource('s3')

    # Creating the Bucket
    s3.create_bucket(Bucket=bucket_name)

Create_Bucket()