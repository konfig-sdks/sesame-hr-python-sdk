# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.schedule_v1_absence_day_off_requests_id_accept.post import AcceptRequest
from sesame_hr_python_sdk.paths.schedule_v1_absence_day_off_requests.post import CreateDayOffRequest
from sesame_hr_python_sdk.paths.schedule_v1_absence_day_off_requests_id.delete import DeleteRequestById
from sesame_hr_python_sdk.paths.schedule_v1_absence_day_off_requests.get import ListDayOffRequests
from sesame_hr_python_sdk.paths.schedule_v1_absence_day_off_requests_id_reject.post import RejectRequest
from sesame_hr_python_sdk.apis.tags.absence_day_off_requests_api_raw import AbsenceDayOffRequestsApiRaw


class AbsenceDayOffRequestsApi(
    AcceptRequest,
    CreateDayOffRequest,
    DeleteRequestById,
    ListDayOffRequests,
    RejectRequest,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AbsenceDayOffRequestsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AbsenceDayOffRequestsApiRaw(api_client)
