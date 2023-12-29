def instance_class(instance_type):
    '''Extract the instance class (e.g. t2, t3) from the full instance type'''
    return instance_type.split('.',1)[0]

class FilterModule(object):
    ''' Custom Ansible tests '''

    def filters(self):
        return {
            'instance_class': instance_class,
        }
