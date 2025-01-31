# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.schedule_v1_absence_calendars.post import CreateCalendar
from sesame_hr_python_sdk.paths.schedule_v1_absence_calendars.get import List
from sesame_hr_python_sdk.paths.schedule_v1_absence_calendars_id.put import UpdateById
from sesame_hr_python_sdk.apis.tags.absence_calendars_api_raw import AbsenceCalendarsApiRaw


class AbsenceCalendarsApi(
    CreateCalendar,
    List,
    UpdateById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AbsenceCalendarsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AbsenceCalendarsApiRaw(api_client)
