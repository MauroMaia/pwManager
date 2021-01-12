from ext.persistence.json.domain.vault_group import Group


def find_group_by_name(group: Group, group_name=None):
    assert group_name is not None, 'group_name should not be None'
    assert group_name != '', 'group_name should not be empty'
    assert type(group_name) == str, 'group_name type need to be string'

    group_list = []
    for user in group.name:
        if user.username == group_name:
            group_list.append(group)
    return group_list
