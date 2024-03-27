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

from sesame_hr_python_sdk.type.work_breaks_list_response_data import WorkBreaksListResponseData
from sesame_hr_python_sdk.type.work_breaks_list_response_meta import WorkBreaksListResponseMeta

class RequiredWorkBreaksListResponse(TypedDict):
    pass

class OptionalWorkBreaksListResponse(TypedDict, total=False):
    data: WorkBreaksListResponseData

    meta: WorkBreaksListResponseMeta

class WorkBreaksListResponse(RequiredWorkBreaksListResponse, OptionalWorkBreaksListResponse):
    pass
