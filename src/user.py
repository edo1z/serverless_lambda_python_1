import json

def users(event, context):
    users = [{"id":1, "name":"taro"}, {"id":2, "name":"jiro"}]
    response = {"statusCode": 200, "body": json.dumps(users)}
    return response