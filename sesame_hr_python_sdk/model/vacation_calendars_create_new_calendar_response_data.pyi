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


class VacationCalendarsCreateNewCalendarResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
        
            @staticmethod
            def employee() -> typing.Type['VacationCalendarsCreateNewCalendarResponseDataEmployee']:
                return VacationCalendarsCreateNewCalendarResponseDataEmployee
        
            @staticmethod
            def daysOff() -> typing.Type['VacationCalendarsCreateNewCalendarResponseDataDaysOff']:
                return VacationCalendarsCreateNewCalendarResponseDataDaysOff
            maxDaysOff = schemas.IntSchema
            year = schemas.IntSchema
        
            @staticmethod
            def vacationConfiguration() -> typing.Type['VacationCalendarsCreateNewCalendarResponseDataVacationConfiguration']:
                return VacationCalendarsCreateNewCalendarResponseDataVacationConfiguration
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            deletedAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "employee": employee,
                "daysOff": daysOff,
                "maxDaysOff": maxDaysOff,
                "year": year,
                "vacationConfiguration": vacationConfiguration,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "deletedAt": deletedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'VacationCalendarsCreateNewCalendarResponseDataEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daysOff"]) -> 'VacationCalendarsCreateNewCalendarResponseDataDaysOff': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDaysOff"]) -> MetaOapg.properties.maxDaysOff: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacationConfiguration"]) -> 'VacationCalendarsCreateNewCalendarResponseDataVacationConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletedAt"]) -> MetaOapg.properties.deletedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "employee", "daysOff", "maxDaysOff", "year", "vacationConfiguration", "createdAt", "updatedAt", "deletedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['VacationCalendarsCreateNewCalendarResponseDataEmployee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daysOff"]) -> typing.Union['VacationCalendarsCreateNewCalendarResponseDataDaysOff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDaysOff"]) -> typing.Union[MetaOapg.properties.maxDaysOff, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> typing.Union[MetaOapg.properties.year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacationConfiguration"]) -> typing.Union['VacationCalendarsCreateNewCalendarResponseDataVacationConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletedAt"]) -> typing.Union[MetaOapg.properties.deletedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "employee", "daysOff", "maxDaysOff", "year", "vacationConfiguration", "createdAt", "updatedAt", "deletedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employee: typing.Union['VacationCalendarsCreateNewCalendarResponseDataEmployee', schemas.Unset] = schemas.unset,
        daysOff: typing.Union['VacationCalendarsCreateNewCalendarResponseDataDaysOff', schemas.Unset] = schemas.unset,
        maxDaysOff: typing.Union[MetaOapg.properties.maxDaysOff, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        vacationConfiguration: typing.Union['VacationCalendarsCreateNewCalendarResponseDataVacationConfiguration', schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        deletedAt: typing.Union[MetaOapg.properties.deletedAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VacationCalendarsCreateNewCalendarResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            employee=employee,
            daysOff=daysOff,
            maxDaysOff=maxDaysOff,
            year=year,
            vacationConfiguration=vacationConfiguration,
            createdAt=createdAt,
            updatedAt=updatedAt,
            deletedAt=deletedAt,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.vacation_calendars_create_new_calendar_response_data_days_off import VacationCalendarsCreateNewCalendarResponseDataDaysOff
from sesame_hr_python_sdk.model.vacation_calendars_create_new_calendar_response_data_employee import VacationCalendarsCreateNewCalendarResponseDataEmployee
from sesame_hr_python_sdk.model.vacation_calendars_create_new_calendar_response_data_vacation_configuration import VacationCalendarsCreateNewCalendarResponseDataVacationConfiguration
