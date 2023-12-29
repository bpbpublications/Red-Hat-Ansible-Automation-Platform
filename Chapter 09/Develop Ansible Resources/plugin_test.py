from ansible import errors
from collections.abc import MutableMapping

def is_large(item):
    '''Determine if instance_type is large, 2xlarge, etc.'''
    if not isinstance(item, MutableMapping):
        raise errors.AnsibleFilterError("The 'is_large' test expects a dictionary")
    if not 'value' in item:
        raise errors.AnsibleFilterError("Unexpected dictionary")
    value = item.get('value', {})
    if not 'instance_type' in value:
        raise errors.AnsibleFilterError("No 'instance_type' was found")
    return 'large' in value.get('instance_type', '')

class TestModule(object):
    ''' Custom Ansible tests '''

    def tests(self):
        return {
            'is_large': is_large,
        }
