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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sesame_hr_python_sdk.pydantic.offices_create_office_request_coordinates import OfficesCreateOfficeRequestCoordinates

class OfficesCreateOfficeRequest(BaseModel):
    # The ID of the company
    company_id: str = Field(alias='companyId')

    # The name of the office
    name: str = Field(alias='name')

    # The description of the office
    description: typing.Optional[str] = Field(None, alias='description')

    # The address of the office
    address: typing.Optional[str] = Field(None, alias='address')

    coordinates: typing.Optional[OfficesCreateOfficeRequestCoordinates] = Field(None, alias='coordinates')

    # The radio of the office
    radio: typing.Optional[int] = Field(None, alias='radio')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
