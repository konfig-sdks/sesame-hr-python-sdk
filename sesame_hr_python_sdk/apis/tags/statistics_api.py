# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.schedule_v1_reports_worked_absence_days.get import ListWorkedAbsenceDaysByEmployee
from sesame_hr_python_sdk.paths.schedule_v1_reports_worked_hours.get import ListWorkedHoursByEmployee
from sesame_hr_python_sdk.paths.schedule_v1_reports_worked_hours_by_week_day.get import ListWorkedHoursByWeekDay
from sesame_hr_python_sdk.paths.schedule_v1_reports_worked_night_hours.get import ListWorkedNightHours
from sesame_hr_python_sdk.apis.tags.statistics_api_raw import StatisticsApiRaw


class StatisticsApi(
    ListWorkedAbsenceDaysByEmployee,
    ListWorkedHoursByEmployee,
    ListWorkedHoursByWeekDay,
    ListWorkedNightHours,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: StatisticsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = StatisticsApiRaw(api_client)
