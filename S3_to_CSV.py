import boto3
import csv
from datetime import datetime
import logging

# Log Configuration
logging.basicConfig(
    filename="s3_csv.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",datefmt='%d/%m/%Y %I:%M:%S'
    )

def s3_csv():
    print('|-----------------------|')
    print('|   Listing Buckets     |')
    print('|-----------------------|')
    # Listing the buckets
    s3 = boto3.resource('s3')
    logging.debug(s3)
    for bucket in s3.buckets.all():
        list = bucket.name
        logging.debug(list)
        print(list)

    # Buckets that will use
    print('--------------------------------')
    bucket_name = input('Tell me which bucket you want to use ')
    logging.debug(bucket_name)

    # Creates the CSV plus day and time that was generated..
    now = datetime.now()
    d1 = now.strftime("Dia_%d_%m_%Y_Hora_%H_%M_%S")
    logging.debug(d1)
    csv_name = bucket_name+'_'+d1+'.csv'
    logging.debug(csv_name)

    # Create to CSV instance
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')

    # Open a CSV with Writing (E) Line Break (NEWLINE)
    my_file = open(csv_name, 'w', newline='')
    logging.debug(my_file)

    # File goes to write CSV
    my_file.writer = csv.writer(my_file, dialect='myDialect')
    logging.debug(my_file)

    # Write on each line creating the header
    my_file.writer.writerow(['bucket_name','status','usr_id','bkp','mach_id','bkpset','arquivo','tamanho','data_modificacao','etag','storage'])
    logging.debug(my_file)

    # Creating the customer
    s3 = boto3.client('s3')
    logging.debug(s3)
	
    # Listing objects inside the bucket
    answer = s3.list_objects_v2(Bucket=bucket_name)
    logging.debug(answer)

    for arquivos in answer['Contents']:
        lstKay = arquivos['Key']
        lstSize = arquivos['Size']
        lastModefield = arquivos['LastModified']
        lastEtag = arquivos['ETag']
        lasStore = arquivos['StorageClass']
        logging.debug(lstKay)
        logging.debug(lstSize)
        logging.debug(lastModefield)
        logging.debug(lastEtag)
        logging.debug(lasStore)
        if lstSize > 0:
            stripped = lstKay.split('/')

            ln = [str(bucket_name)] + stripped + [int(lstSize)] + [str(lastModefield)[0:16]] + [lastEtag.replace('"','')] + [lasStore]
            logging.debug(ln)
            # Performs writing within the for
            my_file.writer.writerow(ln)

    my_file.close()

s3_csv()