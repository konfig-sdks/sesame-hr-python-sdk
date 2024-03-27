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


class ProjectsCreateProjectResponseDataParentProjectManagerCustomFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ProjectsCreateProjectResponseDataParentProjectManagerCustomFieldsItem']:
            return ProjectsCreateProjectResponseDataParentProjectManagerCustomFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ProjectsCreateProjectResponseDataParentProjectManagerCustomFieldsItem'], typing.List['ProjectsCreateProjectResponseDataParentProjectManagerCustomFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProjectsCreateProjectResponseDataParentProjectManagerCustomFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ProjectsCreateProjectResponseDataParentProjectManagerCustomFieldsItem':
        return super().__getitem__(i)

from sesame_hr_python_sdk.model.projects_create_project_response_data_parent_project_manager_custom_fields_item import ProjectsCreateProjectResponseDataParentProjectManagerCustomFieldsItem
