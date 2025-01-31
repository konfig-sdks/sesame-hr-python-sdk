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

from sesame_hr_python_sdk.type.offices_get_all_response_data_item_coordinates import OfficesGetAllResponseDataItemCoordinates

class RequiredOfficesGetAllResponseDataItem(TypedDict):
    pass

class OptionalOfficesGetAllResponseDataItem(TypedDict, total=False):
    description: str

    id: str

    name: str

    address: str

    coordinates: OfficesGetAllResponseDataItemCoordinates

    radio: int

class OfficesGetAllResponseDataItem(RequiredOfficesGetAllResponseDataItem, OptionalOfficesGetAllResponseDataItem):
    pass
