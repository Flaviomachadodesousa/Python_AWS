import boto3

def list_bucket_S3():

    # Resource
    s3 = boto3.resource('s3')

    
    for bucket in s3.buckets.all():
        lst = bucket.name
        
        print(lst)

list_bucket_S3()