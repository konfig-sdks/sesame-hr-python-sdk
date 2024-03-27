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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sesame_hr_python_sdk.pydantic.recruitment_get_candidate_by_id_response_data_vacancy_category import RecruitmentGetCandidateByIdResponseDataVacancyCategory
from sesame_hr_python_sdk.pydantic.recruitment_get_candidate_by_id_response_data_vacancy_location_vacancy import RecruitmentGetCandidateByIdResponseDataVacancyLocationVacancy
from sesame_hr_python_sdk.pydantic.recruitment_get_candidate_by_id_response_data_vacancy_schedule_type import RecruitmentGetCandidateByIdResponseDataVacancyScheduleType

class RecruitmentGetCandidateByIdResponseDataVacancy(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    name: typing.Optional[str] = Field(None, alias='name')

    department: typing.Optional[str] = Field(None, alias='department')

    contact_type: typing.Optional[str] = Field(None, alias='contactType')

    experience: typing.Optional[str] = Field(None, alias='experience')

    created_by_id: typing.Optional[str] = Field(None, alias='createdById')

    status: typing.Optional[Literal["open", "closed", "draft"]] = Field(None, alias='status')

    opened_at: typing.Optional[str] = Field(None, alias='openedAt')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    public: typing.Optional[bool] = Field(None, alias='public')

    location_vacancy: typing.Optional[RecruitmentGetCandidateByIdResponseDataVacancyLocationVacancy] = Field(None, alias='locationVacancy')

    schedule_type: typing.Optional[RecruitmentGetCandidateByIdResponseDataVacancyScheduleType] = Field(None, alias='scheduleType')

    category: typing.Optional[RecruitmentGetCandidateByIdResponseDataVacancyCategory] = Field(None, alias='category')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
