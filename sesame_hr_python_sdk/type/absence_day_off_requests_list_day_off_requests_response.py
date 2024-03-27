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

from sesame_hr_python_sdk.type.absence_day_off_requests_list_day_off_requests_response_data import AbsenceDayOffRequestsListDayOffRequestsResponseData
from sesame_hr_python_sdk.type.absence_day_off_requests_list_day_off_requests_response_meta import AbsenceDayOffRequestsListDayOffRequestsResponseMeta

class RequiredAbsenceDayOffRequestsListDayOffRequestsResponse(TypedDict):
    pass

class OptionalAbsenceDayOffRequestsListDayOffRequestsResponse(TypedDict, total=False):
    data: AbsenceDayOffRequestsListDayOffRequestsResponseData

    meta: AbsenceDayOffRequestsListDayOffRequestsResponseMeta

class AbsenceDayOffRequestsListDayOffRequestsResponse(RequiredAbsenceDayOffRequestsListDayOffRequestsResponse, OptionalAbsenceDayOffRequestsListDayOffRequestsResponse):
    pass
