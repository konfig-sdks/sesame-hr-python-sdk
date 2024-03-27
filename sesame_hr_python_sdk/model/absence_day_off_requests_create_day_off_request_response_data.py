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


class AbsenceDayOffRequestsCreateDayOffRequestResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
        
            @staticmethod
            def absenceCalendar() -> typing.Type['AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendar']:
                return AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendar
        
            @staticmethod
            def employee() -> typing.Type['AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee']:
                return AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee
        
            @staticmethod
            def daysOff() -> typing.Type['AbsenceDayOffRequestsCreateDayOffRequestResponseDataDaysOff']:
                return AbsenceDayOffRequestsCreateDayOffRequestResponseDataDaysOff
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "accepted": "ACCEPTED",
                        "rejected": "REJECTED",
                        "pending": "PENDING",
                    }
                
                @schemas.classproperty
                def ACCEPTED(cls):
                    return cls("accepted")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("rejected")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "create": "CREATE",
                        "delete": "DELETE",
                    }
                
                @schemas.classproperty
                def CREATE(cls):
                    return cls("create")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("delete")
            comment = schemas.UUIDSchema
            resolutionComment = schemas.UUIDSchema
            resolvedAt = schemas.StrSchema
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            deletedAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "absenceCalendar": absenceCalendar,
                "employee": employee,
                "daysOff": daysOff,
                "status": status,
                "type": type,
                "comment": comment,
                "resolutionComment": resolutionComment,
                "resolvedAt": resolvedAt,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "deletedAt": deletedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["absenceCalendar"]) -> 'AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendar': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daysOff"]) -> 'AbsenceDayOffRequestsCreateDayOffRequestResponseDataDaysOff': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolutionComment"]) -> MetaOapg.properties.resolutionComment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolvedAt"]) -> MetaOapg.properties.resolvedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletedAt"]) -> MetaOapg.properties.deletedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "absenceCalendar", "employee", "daysOff", "status", "type", "comment", "resolutionComment", "resolvedAt", "createdAt", "updatedAt", "deletedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["absenceCalendar"]) -> typing.Union['AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendar', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daysOff"]) -> typing.Union['AbsenceDayOffRequestsCreateDayOffRequestResponseDataDaysOff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolutionComment"]) -> typing.Union[MetaOapg.properties.resolutionComment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolvedAt"]) -> typing.Union[MetaOapg.properties.resolvedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletedAt"]) -> typing.Union[MetaOapg.properties.deletedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "absenceCalendar", "employee", "daysOff", "status", "type", "comment", "resolutionComment", "resolvedAt", "createdAt", "updatedAt", "deletedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        absenceCalendar: typing.Union['AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendar', schemas.Unset] = schemas.unset,
        employee: typing.Union['AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee', schemas.Unset] = schemas.unset,
        daysOff: typing.Union['AbsenceDayOffRequestsCreateDayOffRequestResponseDataDaysOff', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, uuid.UUID, schemas.Unset] = schemas.unset,
        resolutionComment: typing.Union[MetaOapg.properties.resolutionComment, str, uuid.UUID, schemas.Unset] = schemas.unset,
        resolvedAt: typing.Union[MetaOapg.properties.resolvedAt, str, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        deletedAt: typing.Union[MetaOapg.properties.deletedAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceDayOffRequestsCreateDayOffRequestResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            absenceCalendar=absenceCalendar,
            employee=employee,
            daysOff=daysOff,
            status=status,
            type=type,
            comment=comment,
            resolutionComment=resolutionComment,
            resolvedAt=resolvedAt,
            createdAt=createdAt,
            updatedAt=updatedAt,
            deletedAt=deletedAt,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.absence_day_off_requests_create_day_off_request_response_data_absence_calendar import AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendar
from sesame_hr_python_sdk.model.absence_day_off_requests_create_day_off_request_response_data_days_off import AbsenceDayOffRequestsCreateDayOffRequestResponseDataDaysOff
from sesame_hr_python_sdk.model.absence_day_off_requests_create_day_off_request_response_data_employee import AbsenceDayOffRequestsCreateDayOffRequestResponseDataEmployee
