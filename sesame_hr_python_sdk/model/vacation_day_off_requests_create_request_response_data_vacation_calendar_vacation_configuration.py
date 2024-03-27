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


class VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfiguration(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            employeeRequestEnabled = schemas.BoolSchema
            needsValidation = schemas.BoolSchema
        
            @staticmethod
            def company() -> typing.Type['VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany']:
                return VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany
            
            
            class dayType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "business_day": "BUSINESS_DAY",
                        "calendar_day": "CALENDAR_DAY",
                    }
                
                @schemas.classproperty
                def BUSINESS_DAY(cls):
                    return cls("business_day")
                
                @schemas.classproperty
                def CALENDAR_DAY(cls):
                    return cls("calendar_day")
            maxDaysOff = schemas.IntSchema
            isDefault = schemas.BoolSchema
        
            @staticmethod
            def notAllowedDateRanges() -> typing.Type['VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges']:
                return VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges
            creationDateNextYear = schemas.StrSchema
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
                "name": name,
                "employeeRequestEnabled": employeeRequestEnabled,
                "needsValidation": needsValidation,
                "company": company,
                "dayType": dayType,
                "maxDaysOff": maxDaysOff,
                "isDefault": isDefault,
                "notAllowedDateRanges": notAllowedDateRanges,
                "creationDateNextYear": creationDateNextYear,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "deletedAt": deletedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeRequestEnabled"]) -> MetaOapg.properties.employeeRequestEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["needsValidation"]) -> MetaOapg.properties.needsValidation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayType"]) -> MetaOapg.properties.dayType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDaysOff"]) -> MetaOapg.properties.maxDaysOff: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notAllowedDateRanges"]) -> 'VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDateNextYear"]) -> MetaOapg.properties.creationDateNextYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletedAt"]) -> MetaOapg.properties.deletedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "employeeRequestEnabled", "needsValidation", "company", "dayType", "maxDaysOff", "isDefault", "notAllowedDateRanges", "creationDateNextYear", "createdAt", "updatedAt", "deletedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeRequestEnabled"]) -> typing.Union[MetaOapg.properties.employeeRequestEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["needsValidation"]) -> typing.Union[MetaOapg.properties.needsValidation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union['VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayType"]) -> typing.Union[MetaOapg.properties.dayType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDaysOff"]) -> typing.Union[MetaOapg.properties.maxDaysOff, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notAllowedDateRanges"]) -> typing.Union['VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDateNextYear"]) -> typing.Union[MetaOapg.properties.creationDateNextYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletedAt"]) -> typing.Union[MetaOapg.properties.deletedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "employeeRequestEnabled", "needsValidation", "company", "dayType", "maxDaysOff", "isDefault", "notAllowedDateRanges", "creationDateNextYear", "createdAt", "updatedAt", "deletedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        employeeRequestEnabled: typing.Union[MetaOapg.properties.employeeRequestEnabled, bool, schemas.Unset] = schemas.unset,
        needsValidation: typing.Union[MetaOapg.properties.needsValidation, bool, schemas.Unset] = schemas.unset,
        company: typing.Union['VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany', schemas.Unset] = schemas.unset,
        dayType: typing.Union[MetaOapg.properties.dayType, str, schemas.Unset] = schemas.unset,
        maxDaysOff: typing.Union[MetaOapg.properties.maxDaysOff, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        notAllowedDateRanges: typing.Union['VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges', schemas.Unset] = schemas.unset,
        creationDateNextYear: typing.Union[MetaOapg.properties.creationDateNextYear, str, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        deletedAt: typing.Union[MetaOapg.properties.deletedAt, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfiguration':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            employeeRequestEnabled=employeeRequestEnabled,
            needsValidation=needsValidation,
            company=company,
            dayType=dayType,
            maxDaysOff=maxDaysOff,
            isDefault=isDefault,
            notAllowedDateRanges=notAllowedDateRanges,
            creationDateNextYear=creationDateNextYear,
            createdAt=createdAt,
            updatedAt=updatedAt,
            deletedAt=deletedAt,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.vacation_day_off_requests_create_request_response_data_vacation_calendar_vacation_configuration_company import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany
from sesame_hr_python_sdk.model.vacation_day_off_requests_create_request_response_data_vacation_calendar_vacation_configuration_not_allowed_date_ranges import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges
