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

from sesame_hr_python_sdk.type.employee_office_assignations_assign_employee_to_office_response_data_employee_company import EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployeeCompany
from sesame_hr_python_sdk.type.employee_office_assignations_assign_employee_to_office_response_data_employee_custom_fields import EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployeeCustomFields

class RequiredEmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployee(TypedDict):
    pass

class OptionalEmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployee(TypedDict, total=False):
    # The description of the employee
    description: str

    id: str

    firstName: str

    lastName: str

    email: str

    workStatus: str

    imageProfileURL: str

    code: int

    pin: int

    phone: str

    company: EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployeeCompany

    gender: str

    # The identifier of your internal employee contract
    contractId: str

    # The National Identity Document of the employee
    nid: str

    identityNumberType: str

    # The Social Security Number of the employee
    ssn: str

    # The Price per hour of the employee
    pricePerHour: typing.Union[int, float]

    # The Account Number of the employee
    accountNumber: str

    dateOfBirth: date

    customFields: EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployeeCustomFields

    createdAt: str

    updatedAt: str

    status: str

    children: int

    disability: int

    # The Address of the employee
    address: str

    # The postal code of the employee
    postalCode: str

    # The city of the employee
    city: str

    # The province of the employee
    province: str

    # The country of the employee
    country: str

    # The nationality of the employee
    nationality: str

    personalMail: typing.Optional[str]

    maritalStatus: str

    # The emergency phone of the employee
    emergencyPhone: str

    # The salary range of the employee
    salaryRange: str

    # The study level of the employee
    studyLevel: str

    # The professional category code of the employee
    professionalCategoryCode: str

    # The professional category description of the employee
    professionalCategoryDescription: str

    bic: str

class EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployee(RequiredEmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployee, OptionalEmployeeOfficeAssignationsAssignEmployeeToOfficeResponseDataEmployee):
    pass
