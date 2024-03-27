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

from sesame_hr_python_sdk.type.offices_update_by_id_response_data_coordinates import OfficesUpdateByIdResponseDataCoordinates

class RequiredOfficesUpdateByIdResponseData(TypedDict):
    pass

class OptionalOfficesUpdateByIdResponseData(TypedDict, total=False):
    description: str

    id: str

    name: str

    address: str

    coordinates: OfficesUpdateByIdResponseDataCoordinates

    radio: int

class OfficesUpdateByIdResponseData(RequiredOfficesUpdateByIdResponseData, OptionalOfficesUpdateByIdResponseData):
    pass
