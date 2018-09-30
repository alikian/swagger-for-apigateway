import boto3
import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

def export(event, context):
    client = boto3.client('apigateway')
    path_parameters = event['pathParameters']
    logger.info(path_parameters)

    restApiIdParam = path_parameters['restApiId']
    path_stage = path_parameters['stage']
    responseSwagger = client.get_export(restApiId=restApiIdParam,stageName=path_stage,exportType='swagger',accepts='application/json')

    response = {
        "statusCode": 200,
        "body": responseSwagger['body'].read().decode("utf-8"),
        "headers": {
            'Content-Type': 'application/json'
        }
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
