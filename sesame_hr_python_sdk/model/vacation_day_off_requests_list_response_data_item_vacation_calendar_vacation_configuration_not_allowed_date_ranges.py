# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sesame_hr_python_sdk import schemas  # noqa: F401


class VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRanges(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRangesItem']:
            return VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRangesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRangesItem'], typing.List['VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRangesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRanges':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRangesItem':
        return super().__getitem__(i)

from sesame_hr_python_sdk.model.vacation_day_off_requests_list_response_data_item_vacation_calendar_vacation_configuration_not_allowed_date_ranges_item import VacationDayOffRequestsListResponseDataItemVacationCalendarVacationConfigurationNotAllowedDateRangesItem
