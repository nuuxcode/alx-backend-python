#!/usr/bin/env python3
""" doc doc doc """
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """doc doc doc"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """doc doc doc"""
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, {"payload": True})
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
