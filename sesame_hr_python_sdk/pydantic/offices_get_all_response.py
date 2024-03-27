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

from sesame_hr_python_sdk.pydantic.offices_get_all_response_data import OfficesGetAllResponseData
from sesame_hr_python_sdk.pydantic.offices_get_all_response_meta import OfficesGetAllResponseMeta

class OfficesGetAllResponse(BaseModel):
    data: typing.Optional[OfficesGetAllResponseData] = Field(None, alias='data')

    meta: typing.Optional[OfficesGetAllResponseMeta] = Field(None, alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
