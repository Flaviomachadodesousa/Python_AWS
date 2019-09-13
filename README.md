# Python_AWS
<br/>

**Installing**
1. Perform the installation of Boto3
   - pip install boto3
<br />

**Configuration**
1. You must configure authentication credentials. Credentials for your AWS account can be found on the IAM console.
   - Create a file with your credentials em ~/.aws/credentials:
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
2. File Create_Mysql.py
   - Inform CSV that was generated with previous python file (S3_to_CSV.py)
	 - Initiate mysql connection
	   - If the mysql connection is correct the message "connected" will appear
		 - Enter table name to create
		   - If the table is correct, it will execute the query and report that it was done successfully
			 - If entered wrong will display the error failed to create the table
<br />
3. File S3_to_CSV.py
   - Inform CSV that was generated with previous python file (S3_to_CSV.py)
	 - Initiate mysql connection
	   - If the mysql connection is correct the message "connected" will appear
		 - Enter the CSV you want to import into the bank
		   - After typing the CSV, the CSV header will be created
		     - After informing the CSV file, it will do the for CSV header created in the previous step and will insert the data
<br />

Version of Python used 3.6

