"""
    Usage: 'ec2-tagging.py  --profile_name <aws_profile_name> --region_name <region_name> --dryrun <True|False>
"""

import argparse
import boto3

def main(args):
    try:
        boto3.setup_default_session(profile_name=args.profile_name, region_name=args.region_name)

        ec2client = boto3.client('ec2')

        response = ec2client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']

                print(f'Checking EC2 instance: {instance_id}')

                if 'Tags' in instance:
                    instance_tags = instance['Tags']
                else:
                    instance_tags = {}               
                
                search_component = search_tags(instance_tags, 'component')
                if search_component is None:
                    if args.dryrun == "True":
                        print(f'\tDRYRUN: Adding "component" tag to: {instance_id}')
                    else:
                        print(f'\tAdding "component" tag to: {instance_id}')
                        ec2client.create_tags(Resources=[instance_id], Tags=[{'Key':'component', 'Value':'<component_name>'}])

                search_product = search_tags(instance_tags, 'product')
                if search_product is None:
                    if args.dryrun == "True":
                        print(f'\tDRYRUN: Adding "product" tag to: {instance_id}')
                    else:
                        print(f'\tAdding "product" tag to: {instance_id}')
                        ec2client.create_tags(Resources=[instance_id], Tags=[{'Key':'product', 'Value':'<product_name>'}])

                search_owner = search_tags(instance_tags, 'owner')
                if search_owner is None:
                    if args.dryrun == "True":
                        print(f'\tDRYRUN: Adding "owner" tag to: {instance_id}')
                    else:
                        print(f'\tAdding "owner" tag to: {instance_id}')
                        ec2client.create_tags(Resources=[instance_id], Tags=[{'Key':'owner', 'Value':'<owner_name>'}])


    except AssertionError as error:
        print(error)


def search_tags(tags, tag_name):
    if tags is None: return None

    return next((sub['Value'] for sub in tags if sub['Key'] == tag_name), None)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile_name', help='aws profile name')
    parser.add_argument('--region_name', help='aws region name')
    parser.add_argument('--dryrun', default="True", help='aws region name')
    args = parser.parse_args()
    main(args)