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

from sesame_hr_python_sdk.type.custom_fields_delete_field_response_meta import CustomFieldsDeleteFieldResponseMeta

class RequiredCustomFieldsDeleteFieldResponse(TypedDict):
    pass

class OptionalCustomFieldsDeleteFieldResponse(TypedDict, total=False):
    data: str

    meta: CustomFieldsDeleteFieldResponseMeta

class CustomFieldsDeleteFieldResponse(RequiredCustomFieldsDeleteFieldResponse, OptionalCustomFieldsDeleteFieldResponse):
    pass
