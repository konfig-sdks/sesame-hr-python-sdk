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


class ProjectsUpdateProjectByIdResponseDataParentProjectManagerCustomFieldsItem(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    name: typing.Optional[str] = Field(None, alias='name')

    slug: typing.Optional[str] = Field(None, alias='slug')

    type: typing.Optional[str] = Field(None, alias='type')

    value: typing.Optional[typing.Union[str]] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
