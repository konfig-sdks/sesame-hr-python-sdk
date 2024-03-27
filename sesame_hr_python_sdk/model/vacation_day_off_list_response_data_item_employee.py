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


class VacationDayOffListResponseDataItemEmployee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.UUIDSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            email = schemas.StrSchema
            
            
            class workStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "online": "ONLINE",
                        "offline": "OFFLINE",
                        "paused": "PAUSED",
                        "remote": "REMOTE",
                    }
                
                @schemas.classproperty
                def ONLINE(cls):
                    return cls("online")
                
                @schemas.classproperty
                def OFFLINE(cls):
                    return cls("offline")
                
                @schemas.classproperty
                def PAUSED(cls):
                    return cls("paused")
                
                @schemas.classproperty
                def REMOTE(cls):
                    return cls("remote")
            imageProfileURL = schemas.StrSchema
            code = schemas.IntSchema
            pin = schemas.IntSchema
            phone = schemas.StrSchema
        
            @staticmethod
            def company() -> typing.Type['VacationDayOffListResponseDataItemEmployeeCompany']:
                return VacationDayOffListResponseDataItemEmployeeCompany
            
            
            class gender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "female": "FEMALE",
                        "male": "MALE",
                        "no_response": "NO_RESPONSE",
                    }
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def NO_RESPONSE(cls):
                    return cls("no_response")
            contractId = schemas.StrSchema
            nid = schemas.StrSchema
            
            
            class identityNumberType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "dni": "DNI",
                        "nie": "NIE",
                        "rut": "RUT",
                        "other": "OTHER",
                    }
                
                @schemas.classproperty
                def DNI(cls):
                    return cls("dni")
                
                @schemas.classproperty
                def NIE(cls):
                    return cls("nie")
                
                @schemas.classproperty
                def RUT(cls):
                    return cls("rut")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
            ssn = schemas.StrSchema
            pricePerHour = schemas.Float32Schema
            accountNumber = schemas.StrSchema
            dateOfBirth = schemas.DateSchema
        
            @staticmethod
            def customFields() -> typing.Type['VacationDayOffListResponseDataItemEmployeeCustomFields']:
                return VacationDayOffListResponseDataItemEmployeeCustomFields
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "active": "ACTIVE",
                        "inactive": "INACTIVE",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("inactive")
            children = schemas.IntSchema
            disability = schemas.IntSchema
            address = schemas.StrSchema
            postalCode = schemas.StrSchema
            city = schemas.StrSchema
            province = schemas.StrSchema
            country = schemas.StrSchema
            nationality = schemas.StrSchema
            
            
            class personalMail(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'email'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'personalMail':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            maritalStatus = schemas.StrSchema
            emergencyPhone = schemas.StrSchema
            salaryRange = schemas.StrSchema
            studyLevel = schemas.StrSchema
            professionalCategoryCode = schemas.StrSchema
            professionalCategoryDescription = schemas.StrSchema
            bic = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "workStatus": workStatus,
                "imageProfileURL": imageProfileURL,
                "code": code,
                "pin": pin,
                "phone": phone,
                "company": company,
                "gender": gender,
                "contractId": contractId,
                "nid": nid,
                "identityNumberType": identityNumberType,
                "ssn": ssn,
                "pricePerHour": pricePerHour,
                "accountNumber": accountNumber,
                "dateOfBirth": dateOfBirth,
                "customFields": customFields,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "status": status,
                "children": children,
                "disability": disability,
                "address": address,
                "postalCode": postalCode,
                "city": city,
                "province": province,
                "country": country,
                "nationality": nationality,
                "personalMail": personalMail,
                "maritalStatus": maritalStatus,
                "emergencyPhone": emergencyPhone,
                "salaryRange": salaryRange,
                "studyLevel": studyLevel,
                "professionalCategoryCode": professionalCategoryCode,
                "professionalCategoryDescription": professionalCategoryDescription,
                "bic": bic,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workStatus"]) -> MetaOapg.properties.workStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageProfileURL"]) -> MetaOapg.properties.imageProfileURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pin"]) -> MetaOapg.properties.pin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'VacationDayOffListResponseDataItemEmployeeCompany': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nid"]) -> MetaOapg.properties.nid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identityNumberType"]) -> MetaOapg.properties.identityNumberType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricePerHour"]) -> MetaOapg.properties.pricePerHour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNumber"]) -> MetaOapg.properties.accountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfBirth"]) -> MetaOapg.properties.dateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'VacationDayOffListResponseDataItemEmployeeCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["children"]) -> MetaOapg.properties.children: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disability"]) -> MetaOapg.properties.disability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["province"]) -> MetaOapg.properties.province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalMail"]) -> MetaOapg.properties.personalMail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maritalStatus"]) -> MetaOapg.properties.maritalStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emergencyPhone"]) -> MetaOapg.properties.emergencyPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryRange"]) -> MetaOapg.properties.salaryRange: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["studyLevel"]) -> MetaOapg.properties.studyLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["professionalCategoryCode"]) -> MetaOapg.properties.professionalCategoryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["professionalCategoryDescription"]) -> MetaOapg.properties.professionalCategoryDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bic"]) -> MetaOapg.properties.bic: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "firstName", "lastName", "email", "workStatus", "imageProfileURL", "code", "pin", "phone", "company", "gender", "contractId", "nid", "identityNumberType", "ssn", "pricePerHour", "accountNumber", "dateOfBirth", "customFields", "createdAt", "updatedAt", "status", "children", "disability", "address", "postalCode", "city", "province", "country", "nationality", "personalMail", "maritalStatus", "emergencyPhone", "salaryRange", "studyLevel", "professionalCategoryCode", "professionalCategoryDescription", "bic", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workStatus"]) -> typing.Union[MetaOapg.properties.workStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageProfileURL"]) -> typing.Union[MetaOapg.properties.imageProfileURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pin"]) -> typing.Union[MetaOapg.properties.pin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union['VacationDayOffListResponseDataItemEmployeeCompany', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractId"]) -> typing.Union[MetaOapg.properties.contractId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nid"]) -> typing.Union[MetaOapg.properties.nid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identityNumberType"]) -> typing.Union[MetaOapg.properties.identityNumberType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> typing.Union[MetaOapg.properties.ssn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricePerHour"]) -> typing.Union[MetaOapg.properties.pricePerHour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNumber"]) -> typing.Union[MetaOapg.properties.accountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfBirth"]) -> typing.Union[MetaOapg.properties.dateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['VacationDayOffListResponseDataItemEmployeeCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["children"]) -> typing.Union[MetaOapg.properties.children, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disability"]) -> typing.Union[MetaOapg.properties.disability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["province"]) -> typing.Union[MetaOapg.properties.province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality"]) -> typing.Union[MetaOapg.properties.nationality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalMail"]) -> typing.Union[MetaOapg.properties.personalMail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maritalStatus"]) -> typing.Union[MetaOapg.properties.maritalStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emergencyPhone"]) -> typing.Union[MetaOapg.properties.emergencyPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryRange"]) -> typing.Union[MetaOapg.properties.salaryRange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["studyLevel"]) -> typing.Union[MetaOapg.properties.studyLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["professionalCategoryCode"]) -> typing.Union[MetaOapg.properties.professionalCategoryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["professionalCategoryDescription"]) -> typing.Union[MetaOapg.properties.professionalCategoryDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bic"]) -> typing.Union[MetaOapg.properties.bic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "firstName", "lastName", "email", "workStatus", "imageProfileURL", "code", "pin", "phone", "company", "gender", "contractId", "nid", "identityNumberType", "ssn", "pricePerHour", "accountNumber", "dateOfBirth", "customFields", "createdAt", "updatedAt", "status", "children", "disability", "address", "postalCode", "city", "province", "country", "nationality", "personalMail", "maritalStatus", "emergencyPhone", "salaryRange", "studyLevel", "professionalCategoryCode", "professionalCategoryDescription", "bic", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        workStatus: typing.Union[MetaOapg.properties.workStatus, str, schemas.Unset] = schemas.unset,
        imageProfileURL: typing.Union[MetaOapg.properties.imageProfileURL, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pin: typing.Union[MetaOapg.properties.pin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        company: typing.Union['VacationDayOffListResponseDataItemEmployeeCompany', schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        contractId: typing.Union[MetaOapg.properties.contractId, str, schemas.Unset] = schemas.unset,
        nid: typing.Union[MetaOapg.properties.nid, str, schemas.Unset] = schemas.unset,
        identityNumberType: typing.Union[MetaOapg.properties.identityNumberType, str, schemas.Unset] = schemas.unset,
        ssn: typing.Union[MetaOapg.properties.ssn, str, schemas.Unset] = schemas.unset,
        pricePerHour: typing.Union[MetaOapg.properties.pricePerHour, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        accountNumber: typing.Union[MetaOapg.properties.accountNumber, str, schemas.Unset] = schemas.unset,
        dateOfBirth: typing.Union[MetaOapg.properties.dateOfBirth, str, date, schemas.Unset] = schemas.unset,
        customFields: typing.Union['VacationDayOffListResponseDataItemEmployeeCustomFields', schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        children: typing.Union[MetaOapg.properties.children, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        disability: typing.Union[MetaOapg.properties.disability, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        province: typing.Union[MetaOapg.properties.province, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        nationality: typing.Union[MetaOapg.properties.nationality, str, schemas.Unset] = schemas.unset,
        personalMail: typing.Union[MetaOapg.properties.personalMail, None, str, schemas.Unset] = schemas.unset,
        maritalStatus: typing.Union[MetaOapg.properties.maritalStatus, str, schemas.Unset] = schemas.unset,
        emergencyPhone: typing.Union[MetaOapg.properties.emergencyPhone, str, schemas.Unset] = schemas.unset,
        salaryRange: typing.Union[MetaOapg.properties.salaryRange, str, schemas.Unset] = schemas.unset,
        studyLevel: typing.Union[MetaOapg.properties.studyLevel, str, schemas.Unset] = schemas.unset,
        professionalCategoryCode: typing.Union[MetaOapg.properties.professionalCategoryCode, str, schemas.Unset] = schemas.unset,
        professionalCategoryDescription: typing.Union[MetaOapg.properties.professionalCategoryDescription, str, schemas.Unset] = schemas.unset,
        bic: typing.Union[MetaOapg.properties.bic, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VacationDayOffListResponseDataItemEmployee':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            firstName=firstName,
            lastName=lastName,
            email=email,
            workStatus=workStatus,
            imageProfileURL=imageProfileURL,
            code=code,
            pin=pin,
            phone=phone,
            company=company,
            gender=gender,
            contractId=contractId,
            nid=nid,
            identityNumberType=identityNumberType,
            ssn=ssn,
            pricePerHour=pricePerHour,
            accountNumber=accountNumber,
            dateOfBirth=dateOfBirth,
            customFields=customFields,
            createdAt=createdAt,
            updatedAt=updatedAt,
            status=status,
            children=children,
            disability=disability,
            address=address,
            postalCode=postalCode,
            city=city,
            province=province,
            country=country,
            nationality=nationality,
            personalMail=personalMail,
            maritalStatus=maritalStatus,
            emergencyPhone=emergencyPhone,
            salaryRange=salaryRange,
            studyLevel=studyLevel,
            professionalCategoryCode=professionalCategoryCode,
            professionalCategoryDescription=professionalCategoryDescription,
            bic=bic,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.vacation_day_off_list_response_data_item_employee_company import VacationDayOffListResponseDataItemEmployeeCompany
from sesame_hr_python_sdk.model.vacation_day_off_list_response_data_item_employee_custom_fields import VacationDayOffListResponseDataItemEmployeeCustomFields
