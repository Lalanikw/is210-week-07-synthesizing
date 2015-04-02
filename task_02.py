#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""clients and their appointment reminders."""


def prepare_email(appointments):
    """reminder draft.
    Args:
        appointments (list): tuples of client names and appointments

    Returns:
        str: reminder information

    Example:
        >>>prepare_email ('jen', '2015')
            Dear jen,
            I look forward to meeting with you on 2015.
            BEST,
            Me
    """
    retval = []
    template = 'Dear {}, \nI look forward to meeting with you on {}.\nBEST,\nMe'
    for appointment in appointments:
        retval.append(template.format(appointment[0], appointment[1]))
    return retval
