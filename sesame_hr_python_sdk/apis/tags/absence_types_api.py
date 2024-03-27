# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.schedule_v1_absence_types.get import List
from sesame_hr_python_sdk.apis.tags.absence_types_api_raw import AbsenceTypesApiRaw


class AbsenceTypesApi(
    List,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AbsenceTypesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AbsenceTypesApiRaw(api_client)
