import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('HTTP trigger - discrete')

    logging.info(req.get_body().decode('utf-8'))

    return func.HttpResponse(status_code=204)
