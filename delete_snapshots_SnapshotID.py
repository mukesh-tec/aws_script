
###Delete sanpshots for given snapshotID in text file###

def lambda_handler(event, context): 
    import boto3
    import datetime
    region = 'ap-south-1'
    owner_ids = ['12345678910']

    client = boto3.client('ec2',region_name=region)
    snapshots = client.describe_snapshots(OwnerIds=owner_ids)

    snapshotid_list = []
    with open ("snapshotID.txt") as fobj:
        snapshotid_list = fobj.readlines()

    for snapshot in snapshots['Snapshots']:
        try:
            if snapshot['SnapshotId'] in snapshotid_list:
                #id = snapshot['SnapshotId']
                #client.delete_snapshot(SnapshotId=id)
                print(snapshot['SnapshotId'])
            else:
                pass
        except Exception as e:
            if 'InvalidSnapshot.InUse' in e.message:
                print("skipping this snapshot")
                continue