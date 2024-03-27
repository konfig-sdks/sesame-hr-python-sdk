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

from sesame_hr_python_sdk.pydantic.absence_day_off_requests_create_day_off_request_response_data_employee_company import AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployeeCompany
from sesame_hr_python_sdk.pydantic.absence_day_off_requests_create_day_off_request_response_data_employee_custom_fields import AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployeeCustomFields

class AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee(BaseModel):
    # The description of the employee
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    email: typing.Optional[str] = Field(None, alias='email')

    work_status: typing.Optional[Literal["online", "offline", "paused", "remote"]] = Field(None, alias='workStatus')

    image_profile_u_r_l: typing.Optional[str] = Field(None, alias='imageProfileURL')

    code: typing.Optional[int] = Field(None, alias='code')

    pin: typing.Optional[int] = Field(None, alias='pin')

    phone: typing.Optional[str] = Field(None, alias='phone')

    company: typing.Optional[AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployeeCompany] = Field(None, alias='company')

    gender: typing.Optional[Literal["female", "male", "no_response"]] = Field(None, alias='gender')

    # The identifier of your internal employee contract
    contract_id: typing.Optional[str] = Field(None, alias='contractId')

    # The National Identity Document of the employee
    nid: typing.Optional[str] = Field(None, alias='nid')

    identity_number_type: typing.Optional[Literal["dni", "nie", "rut", "other"]] = Field(None, alias='identityNumberType')

    # The Social Security Number of the employee
    ssn: typing.Optional[str] = Field(None, alias='ssn')

    # The Price per hour of the employee
    price_per_hour: typing.Optional[typing.Union[int, float]] = Field(None, alias='pricePerHour')

    # The Account Number of the employee
    account_number: typing.Optional[str] = Field(None, alias='accountNumber')

    date_of_birth: typing.Optional[date] = Field(None, alias='dateOfBirth')

    custom_fields: typing.Optional[AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployeeCustomFields] = Field(None, alias='customFields')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    status: typing.Optional[Literal["active", "inactive"]] = Field(None, alias='status')

    children: typing.Optional[int] = Field(None, alias='children')

    disability: typing.Optional[int] = Field(None, alias='disability')

    # The Address of the employee
    address: typing.Optional[str] = Field(None, alias='address')

    # The postal code of the employee
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # The city of the employee
    city: typing.Optional[str] = Field(None, alias='city')

    # The province of the employee
    province: typing.Optional[str] = Field(None, alias='province')

    # The country of the employee
    country: typing.Optional[str] = Field(None, alias='country')

    # The nationality of the employee
    nationality: typing.Optional[str] = Field(None, alias='nationality')

    personal_mail: typing.Optional[typing.Optional[str]] = Field(None, alias='personalMail')

    marital_status: typing.Optional[str] = Field(None, alias='maritalStatus')

    # The emergency phone of the employee
    emergency_phone: typing.Optional[str] = Field(None, alias='emergencyPhone')

    # The salary range of the employee
    salary_range: typing.Optional[str] = Field(None, alias='salaryRange')

    # The study level of the employee
    study_level: typing.Optional[str] = Field(None, alias='studyLevel')

    # The professional category code of the employee
    professional_category_code: typing.Optional[str] = Field(None, alias='professionalCategoryCode')

    # The professional category description of the employee
    professional_category_description: typing.Optional[str] = Field(None, alias='professionalCategoryDescription')

    bic: typing.Optional[str] = Field(None, alias='bic')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
