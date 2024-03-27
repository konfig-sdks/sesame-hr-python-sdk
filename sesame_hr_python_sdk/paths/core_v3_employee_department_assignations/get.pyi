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

from sesame_hr_python_sdk.model.employee_department_assignations_list_response import EmployeeDepartmentAssignationsListResponse as EmployeeDepartmentAssignationsListResponseSchema

from sesame_hr_python_sdk.type.employee_department_assignations_list_response import EmployeeDepartmentAssignationsListResponse

from ...api_client import Dictionary
from sesame_hr_python_sdk.pydantic.employee_department_assignations_list_response import EmployeeDepartmentAssignationsListResponse as EmployeeDepartmentAssignationsListResponsePydantic

# Query params
EmployeeIdSchema = schemas.UUIDSchema
DepartmentIdSchema = schemas.UUIDSchema
LimitSchema = schemas.IntSchema
PageSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'employeeId': typing.Union[EmployeeIdSchema, str, uuid.UUID, ],
        'departmentId': typing.Union[DepartmentIdSchema, str, uuid.UUID, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_employee_id = api_client.QueryParameter(
    name="employeeId",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdSchema,
    explode=True,
)
request_query_department_id = api_client.QueryParameter(
    name="departmentId",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentIdSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = EmployeeDepartmentAssignationsListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeeDepartmentAssignationsListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeeDepartmentAssignationsListResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_mapped_args(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if department_id is not None:
            _query_params["departmentId"] = department_id
        if limit is not None:
            _query_params["limit"] = limit
        if page is not None:
            _query_params["page"] = page
        args.query = _query_params
        return args

    async def _alist_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List employee department assignation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_employee_id,
            request_query_department_id,
            request_query_limit,
            request_query_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/core/v3/employee-department-assignations',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List employee department assignation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_employee_id,
            request_query_department_id,
            request_query_limit,
            request_query_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/core/v3/employee-department-assignations',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            employee_id=employee_id,
            department_id=department_id,
            limit=limit,
            page=page,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            employee_id=employee_id,
            department_id=department_id,
            limit=limit,
            page=page,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeeDepartmentAssignationsListResponsePydantic:
        raw_response = await self.raw.alist(
            employee_id=employee_id,
            department_id=department_id,
            limit=limit,
            page=page,
            **kwargs,
        )
        if validate:
            return EmployeeDepartmentAssignationsListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeDepartmentAssignationsListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EmployeeDepartmentAssignationsListResponsePydantic:
        raw_response = self.raw.list(
            employee_id=employee_id,
            department_id=department_id,
            limit=limit,
            page=page,
        )
        if validate:
            return EmployeeDepartmentAssignationsListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeDepartmentAssignationsListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            employee_id=employee_id,
            department_id=department_id,
            limit=limit,
            page=page,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        employee_id: typing.Optional[str] = None,
        department_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            employee_id=employee_id,
            department_id=department_id,
            limit=limit,
            page=page,
        )
        return self._list_oapg(
            query_params=args.query,
        )

