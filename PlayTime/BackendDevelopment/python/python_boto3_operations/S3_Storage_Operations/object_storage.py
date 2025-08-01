# pip install boto3

import os
import logging
from datetime import datetime, timezone, timedelta
from io import BytesIO
from typing import Optional, Union, Any, Dict, List
from botocore.config import Config as BotoConfig
from botocore.exceptions import ClientError
from boto3.session import Session as Boto3Session
from concurrent.futures import ThreadPoolExecutor, as_completed


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ObjectStorage:

    def __init__(self, endpoint: str, access_key: str, secret_access_key: str):
        self._session = Boto3Session()
        self._client = self._session.client(
            "s3",
            endpoint_url = endpoint,
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_access_key,
            config = BotoConfig(
                proxies = {}
            ),
            verify = True
        )

    def list_objects(self, bucket_name: str, directory: str = "") -> Dict[Any, Any]:
        return self._client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=directory
        )

    def list_paginated_objects(self, bucket_name: str, directory: str = "", max_workers: int = 10) -> List[Dict[Any, Any]]:
        continuation_token = None
        objects = []

        def fetch_objects(continuation_token=None):
            list_kwargs = {
                "Bucket": bucket_name,
                "Prefix": directory
            }
            if continuation_token:
                list_kwargs["ContinuationToken"] = continuation_token

            response = self._client.list_objects_v2(**list_kwargs)
            return response

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(fetch_objects, continuation_token): continuation_token}
            while future_to_token:
                for future in as_completed(future_to_token):
                    response = future.result()
                    contents = response.get("Contents", [])
                    object.extend(contents)

                    if response.get("IsTruncated"):
                        continuation_token = response.get("NextContinuationToken")
                        if continuation_token:
                            future_to_token[executor.submit(fetch_objects, continuation_token)] = continuation_token
                    else:
                        del future_to_token[future]
        return objects

    def get(self, bucket_name: str, object_key: str) -> Dict[Any, Any]:
        return self._client.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

    def put(self, bucket_name: str, object_key: str, object_data: Union[bytes, BytesIO]) -> Dict[Any, Any]:
        return self._client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=object_data
        )

    def delete(self, bucket_name: str, object_key: str) -> Dict[Any, Any]:
        return self._client.delete_object(
            Bucket=bucket_name,
            Key=object_key
        )

    def delete_objects(self, bucket_name: str, object_list: List) -> Dict[Any, Any]:
        return self._client.delete_objects(
            Bucket=bucket_name,
            Delete={
                "Objects": object_list
            }
        )

    def delete_old_objects(self, bucket_name: str, time_delta: timedelta):
        responses = []
        time_threashold = datetime.now(timezone.utc) - time_delta
        objects = self.list_paginated_objects(bucket_name)
        for obj in objects:
            last_modified = obj.get("LastModified")
            if last_modified and last_modified < time_threashold:
                response = self.delete(bucket_name, obj.get("Key"))
                responses.append(response)
        return responses

    def upload(self, bucket_name: str, object_key: str, object_data: BytesIO) -> Dict[Any, Any]:
        return self._client.upload_fileobj(
            Bucket=bucket_name,
            Key=object_key,
            Fileobj=object_data
        )

    def upload_file(self, bucket_name: str, file_name: str, object_name: None):
        if object_name is None:
            object_name = os.path.basename(file_name)

        try:
            response = self._client.upload_file(file_name, bucket_name, object_name)
        except ClientError as e:
            logger.exception("Error uploading file")
            return False
        # also you can return response
        # return response
        return True

    def download(self, bucket_name: str, object_key: str) -> BytesIO:
        object_data = BytesIO()
        self._client.download_fileobj(
            Bucket=bucket_name,
            Key=object_key,
            Fileobj=object_data
        )
        return object_data

    def presigned_url(self, bucket_name: str, object_key: str, expiration: int = 3600, method: str = "get_object") -> str:
        return self._client.generate_presigned_url(
            ClientMethod=method,
            Params={
                "Bucket": bucket_name,
                "Key": object_key
            },
            ExpiresIn=expiration
        )
