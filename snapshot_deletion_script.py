### Snapshots Delection before 10 days###
import boto3
import datetime

region = 'us-west-1'
owner_ids = ['12345678']
 
client = boto3.client('ec2',region_name=region)
snapshots = client.describe_snapshots(OwnerIds=owner_ids)
for snapshot in snapshots['Snapshots']:
    snapshot_start_time = snapshot['StartTime']
    snapshot_start_date = snapshot_start_time.date()
    current_date =datetime.datetime.now().date()
    no_of_day = current_date - snapshot_start_date
    try:
    if no_of_day.days>10:
        id = snapshot['SnapshotId']
        client.delete_snapshot(SnapshotId=id)
    except Exception,e:
    if 'InvalidSnapshot.InUse' in e.message:
        print "skipping this snapshot"
        continue
