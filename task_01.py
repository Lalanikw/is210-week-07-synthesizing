#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""party statistics"""


def get_party_stats(families, table_size=6):
    """Party crowd and table arrangement.
    Args:
        families (list): ['Angel', 'Michael', 'Samuel'], ['Jennifer', 'James']
        table_size (int): max '6'

    Returns:
        tuple: ('total', 'table')

    Example:
        >>> get_party_stats(['Jan'], ['Jen','Jess'], ['Jem', 'Jack','Janis'])
            (6, 3)
    """

    total = 0
    tables = 0
    table_size = 6
    print 'families is ', families
    for fam_grp in families:
        total += len(fam_grp)
        tables += len(fam_grp) / table_size
        if len(fam_grp) % table_size > 0:
            tables += 1
    return (total, tables)
