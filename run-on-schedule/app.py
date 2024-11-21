from chalice import Chalice
import boto3

app = Chalice(app_name='run-on-schedule')


@app.lambda_function()
def first_function(event, context):
    return {'hello': 'world'}


@app.lambda_function()
def second_function(event, context):
    return {'hello': 'world2'}


instance_id = "id-1234543456543"
ec2 = boto3.client('ec2')

@app.schedule('cron(0 0 * * *)')
def daily_task():
   print("Running daily task at midnight")
   response = ec2.start_instances(instance_id)
