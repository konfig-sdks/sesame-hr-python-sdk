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

from sesame_hr_python_sdk.type.offices_create_office_request_coordinates import OfficesCreateOfficeRequestCoordinates

class RequiredOfficesCreateOfficeRequest(TypedDict):
    # The ID of the company
    companyId: str

    # The name of the office
    name: str

class OptionalOfficesCreateOfficeRequest(TypedDict, total=False):
    # The description of the office
    description: str

    # The address of the office
    address: str

    coordinates: OfficesCreateOfficeRequestCoordinates

    # The radio of the office
    radio: int

class OfficesCreateOfficeRequest(RequiredOfficesCreateOfficeRequest, OptionalOfficesCreateOfficeRequest):
    pass
