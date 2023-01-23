import logging
import os
import uuid
import azure.functions as func
from azure.storage.blob import ContainerClient, ContentSettings
from lorem_text import lorem

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('HTTP trigger - storage_init')

    conn_str = os.environ['AzureWebJobsStorage']
    container_name = os.environ['StorageContainerName']

    container_client = ContainerClient.from_connection_string(
        conn_str=conn_str, container_name=container_name)

    if container_client.exists():
        container_client.delete_container()

    container_client.create_container()

    for _ in range(0, 100):
        name = str(uuid.uuid4())
        text = lorem.paragraphs(5)
        container_client.upload_blob(
            name=name, data=text, content_settings=ContentSettings(content_type='text/plain'))

    return func.HttpResponse(status_code=204)
