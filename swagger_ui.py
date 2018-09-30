import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

def export(event, context):

    htmlIndex = ''

    with open('index.html', 'r') as myfile:
        htmlIndex = myfile.read()

    logger.info('htmlIndex:')
    logger.info(htmlIndex)


    response = {
        "statusCode": 200,
        "body": htmlIndex,
        "headers": {
            'Content-Type': 'text/html'
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
