# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import sesame_hr_python_sdk
from sesame_hr_python_sdk.paths.recruitment_v1_vacancies import get
from sesame_hr_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRecruitmentV1Vacancies(ApiTestMixin, unittest.TestCase):
    """
    RecruitmentV1Vacancies unit test stubs
        Get vacancies list
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
