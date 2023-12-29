# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
  name: test
  author: Luca Berton <luca@ansiblepilot.com>
  version_added: "0.1"  # same as collection version
  short_description: read API token
  description:
      - This lookup returns the token from the provided API.
"""
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
import requests

display = Display()

class LookupModule(LookupBase):

    _URL_ = "https://reqres.in/api/login"

    def run(self, terms, variables=None, **kwargs):
      payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
      }
      try:
        res = requests.post(self._URL_, data=payload)
        res.raise_for_status()
        ret = res.json()['token']

      except requests.exceptions.HTTPError as e:
        raise AnsibleError('There was an error getting a token. The lookup API returned %s', response.status_code)
      except Exception as e:
        raise AnsibleError('Unhandled exception is lookup plugin. Origin: %s', e)

      return [ret]
