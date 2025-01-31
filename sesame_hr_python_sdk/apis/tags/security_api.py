# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.core_v3_info.get import GetTokenInfo
from sesame_hr_python_sdk.apis.tags.security_api_raw import SecurityApiRaw


class SecurityApi(
    GetTokenInfo,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SecurityApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SecurityApiRaw(api_client)
