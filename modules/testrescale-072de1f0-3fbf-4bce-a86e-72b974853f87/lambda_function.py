import boto3
import botocore
import json
import csv
#import datetime
from datetime import datetime
from dateutil import tz

def lambda_handler(event, context):

    buck_name = "sample-spot-prices"
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(buck_name)
    
    #today = datetime.datetime.today().strftime('%Y%m%d')
    today = datetime.today()
    today_date = get_current_date(today)

    #print(today_date)
    s3upload = boto3.client('s3')
    uploadbucketname = "rescale"
    cnt = 1
    for o in bucket.objects.all():
        key = o.key
        obj = s3.Object(buck_name,key)
        a = obj.get()['Body'].read()
        a = json.loads(a)
        b = key.split(".")
        fnamelist = b[0].split("_")
        fdate= fnamelist[1]
        faccountid = fnamelist[2]
        fregion = fnamelist[3]
        if str(fdate) == str(today_date):
            print("true")
            s3filekey = fdate+'test'+str(cnt)+'.csv'
            #json to csv
            #f = csv.writer(open(fdate+'test'+str(cnt)+'.csv','w'), lineterminator='\n')
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
            s3upload.upload_file('/tmp/'+s3filekey,uploadbucketname,s3filekey)
            
        else:
            #print("true")
            continue;
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully wrote files to S3')
    }


def get_current_date(today):
    from_zone = tz.tzutc()
    to_zone = tz.gettz('America/New_York')
    utctime = datetime.strptime(str(today),'%Y-%m-%d %H:%M:%S.%f')
    utctime = utctime.replace(tzinfo=from_zone)
    est = utctime.astimezone(to_zone)
    current_date = est.strftime('%Y%m%d')
    return current_date