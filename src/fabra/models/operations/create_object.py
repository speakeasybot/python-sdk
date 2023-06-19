"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import object as shared_object
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateObject200ApplicationJSON:
    r"""Successfully created object"""
    
    object: Optional[shared_object.Object] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateObjectResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_object_200_application_json_object: Optional[CreateObject200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully created object"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    