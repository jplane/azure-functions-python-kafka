import logging
import os
import json
import azure.functions as func
from azure.storage.blob import ContainerClient

def main(req: func.HttpRequest, out: func.Out[str]) -> func.HttpResponse:

    logging.info('HTTP trigger - batch_init')

    conn_str = os.environ['AzureWebJobsStorage']
    container_name = os.environ['StorageContainerName']

    container_client = ContainerClient.from_connection_string(
        conn_str=conn_str, container_name=container_name)

    if container_client.exists():
        blobs_list = container_client.list_blobs()
        names = [{ 'container_name': container_name, 'blob_name': blob.name }
                  for blob in blobs_list]
        out.set(json.dumps(names))

    return func.HttpResponse(status_code=204)
