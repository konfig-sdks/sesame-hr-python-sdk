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

from sesame_hr_python_sdk.type.vacation_configurations_list_configurations_response_data_item_company import VacationConfigurationsListConfigurationsResponseDataItemCompany
from sesame_hr_python_sdk.type.vacation_configurations_list_configurations_response_data_item_not_allowed_date_ranges import VacationConfigurationsListConfigurationsResponseDataItemNotAllowedDateRanges

class RequiredVacationConfigurationsListConfigurationsResponseDataItem(TypedDict):
    pass

class OptionalVacationConfigurationsListConfigurationsResponseDataItem(TypedDict, total=False):
    id: str

    name: str

    employeeRequestEnabled: bool

    needsValidation: bool

    company: VacationConfigurationsListConfigurationsResponseDataItemCompany

    dayType: str

    maxDaysOff: int

    isDefault: bool

    notAllowedDateRanges: VacationConfigurationsListConfigurationsResponseDataItemNotAllowedDateRanges

    creationDateNextYear: str

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

class VacationConfigurationsListConfigurationsResponseDataItem(RequiredVacationConfigurationsListConfigurationsResponseDataItem, OptionalVacationConfigurationsListConfigurationsResponseDataItem):
    pass
