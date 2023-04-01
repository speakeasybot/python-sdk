"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createlinktokenresponse as shared_createlinktokenresponse
from typing import Optional


@dataclasses.dataclass
class CreateLinkTokenResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_link_token_response: Optional[shared_createlinktokenresponse.CreateLinkTokenResponse] = dataclasses.field(default=None)
    r"""Successfully created link token"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    