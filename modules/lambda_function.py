import boto3
import botocore
import json
import csv
from datetime import datetime
from dateutil import tz

def lambda_handler(event, context):

    #Source S3 bucket.
    buck_name = "sample-spot-prices"
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(buck_name)

    today = datetime.today()
    today_date = get_current_date(today)
    s3upload = boto3.client('s3')
    uploadbucketname = "rescale"
    cnt = 1
    for o in bucket.objects.all():
        key = o.key
        obj = s3.Object(buck_name,key)

        #parsing the accountid, date and region from the file name
        a = obj.get()['Body'].read()
        a = json.loads(a)
        b = key.split(".")
        fnamelist = b[0].split("_")
        fdate= fnamelist[1]
        faccountid = fnamelist[2]
        fregion = fnamelist[3]

        # reading only files added on the same day
        if str(fdate) == str(today_date):
            print("true")
            s3filekey = fdate+'test'+str(cnt)+'.csv'

            #json to csv
            f= open('/tmp/'+s3filekey,'w',newline='')
            writer = csv.writer(f)
            writer.writerow(["AccountID", "Region","AvailabilityZone","InstanceType","ProductDescription","SpotPrice","Timestamp"])
            cnt+=1
            for x in a:
                writer.writerow([faccountid,
                            fregion,
                            x["AvailabilityZone"],
                            x["InstanceType"],
                            x["ProductDescription"],
                            x["SpotPrice"],
                            x["Timestamp"]])
            f.close()

            #uploading csvv files to new S3 bucket
            s3upload.upload_file('/tmp/'+s3filekey,uploadbucketname,s3filekey)
            
        else:
            continue;

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully wrote files to S3')
    }

# UTC to EST
def get_current_date(today):
    from_zone = tz.tzutc()
    to_zone = tz.gettz('America/New_York')
    utctime = datetime.strptime(str(today),'%Y-%m-%d %H:%M:%S.%f')
    utctime = utctime.replace(tzinfo=from_zone)
    est = utctime.astimezone(to_zone)
    current_date = est.strftime('%Y%m%d')
    return current_date