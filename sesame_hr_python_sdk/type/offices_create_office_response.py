# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from sesame_hr_python_sdk.type.offices_create_office_response_data import OfficesCreateOfficeResponseData
from sesame_hr_python_sdk.type.offices_create_office_response_meta import OfficesCreateOfficeResponseMeta

class RequiredOfficesCreateOfficeResponse(TypedDict):
    pass

class OptionalOfficesCreateOfficeResponse(TypedDict, total=False):
    data: OfficesCreateOfficeResponseData

    meta: OfficesCreateOfficeResponseMeta

class OfficesCreateOfficeResponse(RequiredOfficesCreateOfficeResponse, OptionalOfficesCreateOfficeResponse):
    pass
