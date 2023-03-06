import requests as requests_http
from . import utils
from fabra.models import operations
from typing import Optional

class Destination:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def create_destination(self, request: operations.CreateDestinationRequest) -> operations.CreateDestinationResponse:
        r"""Create a new destination
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/destination'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDestinationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateDestination200ApplicationJSON])
                res.create_destination_200_application_json_object = out
        elif http_res.status_code == 401:
            pass
        elif http_res.status_code == 500:
            pass

        return res

    def get_destinations(self) -> operations.GetDestinationsResponse:
        r"""Get all destinations
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/destinations'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDestinationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDestinations200ApplicationJSON])
                res.get_destinations_200_application_json_object = out
        elif http_res.status_code == 401:
            pass
        elif http_res.status_code == 500:
            pass

        return res

    