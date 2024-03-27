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

from sesame_hr_python_sdk.type.recruitment_get_candidate_status_list_response_data import RecruitmentGetCandidateStatusListResponseData
from sesame_hr_python_sdk.type.recruitment_get_candidate_status_list_response_meta import RecruitmentGetCandidateStatusListResponseMeta

class RequiredRecruitmentGetCandidateStatusListResponse(TypedDict):
    pass

class OptionalRecruitmentGetCandidateStatusListResponse(TypedDict, total=False):
    data: RecruitmentGetCandidateStatusListResponseData

    meta: RecruitmentGetCandidateStatusListResponseMeta

class RecruitmentGetCandidateStatusListResponse(RequiredRecruitmentGetCandidateStatusListResponse, OptionalRecruitmentGetCandidateStatusListResponse):
    pass
