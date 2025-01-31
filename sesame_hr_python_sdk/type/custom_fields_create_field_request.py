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


class RequiredCustomFieldsCreateFieldRequest(TypedDict):
    # The id of the company
    companyId: str

    # The name of the custom field
    name: str

    # The type of the custom field
    type: str

class OptionalCustomFieldsCreateFieldRequest(TypedDict, total=False):
    slug: str

class CustomFieldsCreateFieldRequest(RequiredCustomFieldsCreateFieldRequest, OptionalCustomFieldsCreateFieldRequest):
    pass
