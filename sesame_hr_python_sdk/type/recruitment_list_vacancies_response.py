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

from sesame_hr_python_sdk.type.recruitment_list_vacancies_response_data import RecruitmentListVacanciesResponseData
from sesame_hr_python_sdk.type.recruitment_list_vacancies_response_meta import RecruitmentListVacanciesResponseMeta

class RequiredRecruitmentListVacanciesResponse(TypedDict):
    pass

class OptionalRecruitmentListVacanciesResponse(TypedDict, total=False):
    data: RecruitmentListVacanciesResponseData

    meta: RecruitmentListVacanciesResponseMeta

class RecruitmentListVacanciesResponse(RequiredRecruitmentListVacanciesResponse, OptionalRecruitmentListVacanciesResponse):
    pass
