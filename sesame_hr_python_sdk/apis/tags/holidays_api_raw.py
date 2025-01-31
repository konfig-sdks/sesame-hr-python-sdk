# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.schedule_v1_holidays_holiday_calendar_id_employees.post import AssignToEmployeeRaw
from sesame_hr_python_sdk.paths.schedule_v1_holidays_holiday_calendar_id_employees.get import GetByHolidayCalendarEmployeesRaw
from sesame_hr_python_sdk.paths.schedule_v1_holidays.get import ListRaw
from sesame_hr_python_sdk.paths.schedule_v1_holidays_holiday_calendar_id_employees.delete import UnassignHolidayCalendarToEmployeeRaw


class HolidaysApiRaw(
    AssignToEmployeeRaw,
    GetByHolidayCalendarEmployeesRaw,
    ListRaw,
    UnassignHolidayCalendarToEmployeeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
