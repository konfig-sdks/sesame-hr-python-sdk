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


class ProjectsUpdateProjectByIdResponseDataCustomer(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    customer_name: typing.Optional[str] = Field(None, alias='customerName')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    email: typing.Optional[str] = Field(None, alias='email')

    phone: typing.Optional[str] = Field(None, alias='phone')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[str] = Field(None, alias='deletedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
