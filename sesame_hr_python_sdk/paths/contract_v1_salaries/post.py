# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from sesame_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from sesame_hr_python_sdk.api_response import AsyncGeneratorResponse
from sesame_hr_python_sdk import api_client, exceptions
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

from sesame_hr_python_sdk.model.salaries_create_salary_request import SalariesCreateSalaryRequest as SalariesCreateSalaryRequestSchema
from sesame_hr_python_sdk.model.salaries_create_salary_response import SalariesCreateSalaryResponse as SalariesCreateSalaryResponseSchema

from sesame_hr_python_sdk.type.salaries_create_salary_request import SalariesCreateSalaryRequest
from sesame_hr_python_sdk.type.salaries_create_salary_response import SalariesCreateSalaryResponse

from ...api_client import Dictionary
from sesame_hr_python_sdk.pydantic.salaries_create_salary_response import SalariesCreateSalaryResponse as SalariesCreateSalaryResponsePydantic
from sesame_hr_python_sdk.pydantic.salaries_create_salary_request import SalariesCreateSalaryRequest as SalariesCreateSalaryRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = SalariesCreateSalaryRequestSchema


request_body_salaries_create_salary_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJson = SalariesCreateSalaryResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SalariesCreateSalaryResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SalariesCreateSalaryResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_salary_mapped_args(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if employee_id is not None:
            _body["employeeId"] = employee_id
        if pay_period is not None:
            _body["payPeriod"] = pay_period
        if currency is not None:
            _body["currency"] = currency
        if gross_salary is not None:
            _body["grossSalary"] = gross_salary
        if payments is not None:
            _body["payments"] = payments
        if contribution_group_id is not None:
            _body["contributionGroupId"] = contribution_group_id
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if comments is not None:
            _body["comments"] = comments
        args.body = _body
        return args

    async def _acreate_salary_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Salary
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contract/v1/salaries',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_salaries_create_salary_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_salary_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Salary
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contract/v1/salaries',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_salaries_create_salary_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateSalaryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_salary(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_salary_mapped_args(
            employee_id=employee_id,
            pay_period=pay_period,
            currency=currency,
            gross_salary=gross_salary,
            payments=payments,
            contribution_group_id=contribution_group_id,
            start_date=start_date,
            end_date=end_date,
            comments=comments,
        )
        return await self._acreate_salary_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_salary(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_salary_mapped_args(
            employee_id=employee_id,
            pay_period=pay_period,
            currency=currency,
            gross_salary=gross_salary,
            payments=payments,
            contribution_group_id=contribution_group_id,
            start_date=start_date,
            end_date=end_date,
            comments=comments,
        )
        return self._create_salary_oapg(
            body=args.body,
        )

class CreateSalary(BaseApi):

    async def acreate_salary(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> SalariesCreateSalaryResponsePydantic:
        raw_response = await self.raw.acreate_salary(
            employee_id=employee_id,
            pay_period=pay_period,
            currency=currency,
            gross_salary=gross_salary,
            payments=payments,
            contribution_group_id=contribution_group_id,
            start_date=start_date,
            end_date=end_date,
            comments=comments,
            **kwargs,
        )
        if validate:
            return SalariesCreateSalaryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SalariesCreateSalaryResponsePydantic, raw_response.body)
    
    
    def create_salary(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
        validate: bool = False,
    ) -> SalariesCreateSalaryResponsePydantic:
        raw_response = self.raw.create_salary(
            employee_id=employee_id,
            pay_period=pay_period,
            currency=currency,
            gross_salary=gross_salary,
            payments=payments,
            contribution_group_id=contribution_group_id,
            start_date=start_date,
            end_date=end_date,
            comments=comments,
        )
        if validate:
            return SalariesCreateSalaryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SalariesCreateSalaryResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_salary_mapped_args(
            employee_id=employee_id,
            pay_period=pay_period,
            currency=currency,
            gross_salary=gross_salary,
            payments=payments,
            contribution_group_id=contribution_group_id,
            start_date=start_date,
            end_date=end_date,
            comments=comments,
        )
        return await self._acreate_salary_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        employee_id: str,
        pay_period: str,
        currency: str,
        gross_salary: typing.Union[int, float],
        payments: int,
        contribution_group_id: str,
        start_date: date,
        end_date: typing.Optional[date] = None,
        comments: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_salary_mapped_args(
            employee_id=employee_id,
            pay_period=pay_period,
            currency=currency,
            gross_salary=gross_salary,
            payments=payments,
            contribution_group_id=contribution_group_id,
            start_date=start_date,
            end_date=end_date,
            comments=comments,
        )
        return self._create_salary_oapg(
            body=args.body,
        )

