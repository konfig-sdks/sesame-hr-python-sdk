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


class WorkBreaksListResponseDataItem(BaseModel):
    company_id: typing.Optional[str] = Field(None, alias='companyId')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    color: typing.Optional[str] = Field(None, alias='color')

    icon: typing.Optional[str] = Field(None, alias='icon')

    break_minutes: typing.Optional[int] = Field(None, alias='breakMinutes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
