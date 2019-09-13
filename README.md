# Python_AWS
<br/>
**Installing**
1. Perform the installation of Boto3
   - pip install boto3
<br />

**Configuration**
1. You must configure authentication credentials. Credentials for your AWS account can be found on the IAM console.
   - Crie um arquivos com suas credencias em ~/.aws/credentials:
	 - credentials.file
	   - [default]
		aws_access_key_id = your passkey
		aws_secret_access_key = your password
<br />


**Project performed with AWS Boto3 SDK**
1. File S3_to_CSV.py
   - Lists the buckets existing in your account
	 - Creates a CSV file with the name of the bucket, day and time the CSV was generated
	   - Insert into created CSV name bucket, size, data modified, etag, storage, file,

<br />

Version of Python used 3.6

