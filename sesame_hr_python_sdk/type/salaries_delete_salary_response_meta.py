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


class RequiredSalariesDeleteSalaryResponseMeta(TypedDict):
    pass

class OptionalSalariesDeleteSalaryResponseMeta(TypedDict, total=False):
    currentPage: int

    lastPage: int

    total: int

    perPage: int

class SalariesDeleteSalaryResponseMeta(RequiredSalariesDeleteSalaryResponseMeta, OptionalSalariesDeleteSalaryResponseMeta):
    pass
