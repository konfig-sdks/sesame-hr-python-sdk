# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.schedule_v1_holiday_calendar.post import CreateNewCalendar
from sesame_hr_python_sdk.paths.schedule_v1_holiday_calendar_holiday_calendar_id.get import GetById
from sesame_hr_python_sdk.paths.schedule_v1_holiday_calendar.get import ListCalendar
from sesame_hr_python_sdk.paths.schedule_v1_holiday_calendar_holiday_calendar_id.delete import RemoveById
from sesame_hr_python_sdk.paths.schedule_v1_holiday_calendar_holiday_calendar_id.put import UpdateById
from sesame_hr_python_sdk.apis.tags.holiday_calendars_api_raw import HolidayCalendarsApiRaw


class HolidayCalendarsApi(
    CreateNewCalendar,
    GetById,
    ListCalendar,
    RemoveById,
    UpdateById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: HolidayCalendarsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = HolidayCalendarsApiRaw(api_client)
