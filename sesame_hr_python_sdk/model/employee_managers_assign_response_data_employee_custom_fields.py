# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sesame_hr_python_sdk import schemas  # noqa: F401


class EmployeeManagersAssignResponseDataEmployeeCustomFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EmployeeManagersAssignResponseDataEmployeeCustomFieldsItem']:
            return EmployeeManagersAssignResponseDataEmployeeCustomFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EmployeeManagersAssignResponseDataEmployeeCustomFieldsItem'], typing.List['EmployeeManagersAssignResponseDataEmployeeCustomFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmployeeManagersAssignResponseDataEmployeeCustomFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EmployeeManagersAssignResponseDataEmployeeCustomFieldsItem':
        return super().__getitem__(i)

from sesame_hr_python_sdk.model.employee_managers_assign_response_data_employee_custom_fields_item import EmployeeManagersAssignResponseDataEmployeeCustomFieldsItem
