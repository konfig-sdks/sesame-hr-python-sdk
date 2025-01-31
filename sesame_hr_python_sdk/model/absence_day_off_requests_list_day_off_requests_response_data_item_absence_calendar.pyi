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


class AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendar(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
        
            @staticmethod
            def employee() -> typing.Type['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarEmployee']:
                return AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarEmployee
        
            @staticmethod
            def daysOff() -> typing.Type['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarDaysOff']:
                return AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarDaysOff
            maxDaysOff = schemas.IntSchema
            year = schemas.IntSchema
        
            @staticmethod
            def absenceType() -> typing.Type['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarAbsenceType']:
                return AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarAbsenceType
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            
            
            class deletedAt(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deletedAt':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "employee": employee,
                "daysOff": daysOff,
                "maxDaysOff": maxDaysOff,
                "year": year,
                "absenceType": absenceType,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "deletedAt": deletedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daysOff"]) -> 'AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarDaysOff': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDaysOff"]) -> MetaOapg.properties.maxDaysOff: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["absenceType"]) -> 'AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarAbsenceType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletedAt"]) -> MetaOapg.properties.deletedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "employee", "daysOff", "maxDaysOff", "year", "absenceType", "createdAt", "updatedAt", "deletedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarEmployee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daysOff"]) -> typing.Union['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarDaysOff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDaysOff"]) -> typing.Union[MetaOapg.properties.maxDaysOff, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> typing.Union[MetaOapg.properties.year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["absenceType"]) -> typing.Union['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarAbsenceType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletedAt"]) -> typing.Union[MetaOapg.properties.deletedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "employee", "daysOff", "maxDaysOff", "year", "absenceType", "createdAt", "updatedAt", "deletedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employee: typing.Union['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarEmployee', schemas.Unset] = schemas.unset,
        daysOff: typing.Union['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarDaysOff', schemas.Unset] = schemas.unset,
        maxDaysOff: typing.Union[MetaOapg.properties.maxDaysOff, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        absenceType: typing.Union['AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarAbsenceType', schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        deletedAt: typing.Union[MetaOapg.properties.deletedAt, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendar':
        return super().__new__(
            cls,
            *args,
            id=id,
            employee=employee,
            daysOff=daysOff,
            maxDaysOff=maxDaysOff,
            year=year,
            absenceType=absenceType,
            createdAt=createdAt,
            updatedAt=updatedAt,
            deletedAt=deletedAt,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.absence_day_off_requests_list_day_off_requests_response_data_item_absence_calendar_absence_type import AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarAbsenceType
from sesame_hr_python_sdk.model.absence_day_off_requests_list_day_off_requests_response_data_item_absence_calendar_days_off import AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarDaysOff
from sesame_hr_python_sdk.model.absence_day_off_requests_list_day_off_requests_response_data_item_absence_calendar_employee import AbsenceDayOffRequestsListDayOffRequestsResponseDataItemAbsenceCalendarEmployee
