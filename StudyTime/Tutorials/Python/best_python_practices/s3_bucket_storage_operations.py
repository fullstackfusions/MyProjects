from io import BytesIO
from typing import Optional, Union, Any, Dict
from botocore.config import Config as BotoConfig
from boto3.session import Session as Boto3Session

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
            )
        )

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

    def upload(self, bucket_name: str, object_key: str, object_data: Union[bytes, BytesIO]) -> Dict[Any, Any]:
        return self._client.upload_fileobj(
            Bucket=bucket_name,
            Key=object_key,
            Body=object_data
        )

    def put(self, bucket_name: str, object_key: str) -> BytesIO:
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
