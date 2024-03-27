# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.project_v1_time_entries.post import CreateNewEntryRaw
from sesame_hr_python_sdk.paths.project_v1_time_entries_id.delete import DeleteByIdRaw
from sesame_hr_python_sdk.paths.project_v1_time_entries.get import ListRaw
from sesame_hr_python_sdk.paths.project_v1_time_entries_start.post import StartEntryRaw
from sesame_hr_python_sdk.paths.project_v1_time_entries_stop.post import StopTimeEntryOutRaw
from sesame_hr_python_sdk.paths.project_v1_time_entries_id.put import UpdateEntryRaw


class TimeEntriesApiRaw(
    CreateNewEntryRaw,
    DeleteByIdRaw,
    ListRaw,
    StartEntryRaw,
    StopTimeEntryOutRaw,
    UpdateEntryRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
