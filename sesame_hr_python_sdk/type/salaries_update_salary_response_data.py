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


class RequiredSalariesUpdateSalaryResponseData(TypedDict):
    pass

class OptionalSalariesUpdateSalaryResponseData(TypedDict, total=False):
    id: str

    payPeriod: str

    currency: str

    grossSalary: int

    payments: int

    contributionGroup: str

    startDate: date

    endDate: date

    comments: str

    monthlyGrossSalary: int

    createdAt: str

    updatedAt: str

class SalariesUpdateSalaryResponseData(RequiredSalariesUpdateSalaryResponseData, OptionalSalariesUpdateSalaryResponseData):
    pass
