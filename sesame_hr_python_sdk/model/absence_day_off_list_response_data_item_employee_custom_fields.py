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


class AbsenceDayOffListResponseDataItemEmployeeCustomFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['AbsenceDayOffListResponseDataItemEmployeeCustomFieldsItem']:
            return AbsenceDayOffListResponseDataItemEmployeeCustomFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['AbsenceDayOffListResponseDataItemEmployeeCustomFieldsItem'], typing.List['AbsenceDayOffListResponseDataItemEmployeeCustomFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AbsenceDayOffListResponseDataItemEmployeeCustomFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AbsenceDayOffListResponseDataItemEmployeeCustomFieldsItem':
        return super().__getitem__(i)

from sesame_hr_python_sdk.model.absence_day_off_list_response_data_item_employee_custom_fields_item import AbsenceDayOffListResponseDataItemEmployeeCustomFieldsItem
