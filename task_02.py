#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""clients and their appointment reminders."""


def prepare_email(client_name, appointment):
    """reminder draft.
    Args:
        appointments (tuple): [('list of client's name', 'their appointments')]

    Returns:
        list: 

    Example:
        >>>prepare_email ('jen', '2015')
            Dear jen, 
            I look forward to meeting with you on 2015.
            BEST, 
            Me  
    """
    appointments = [('client_name', 'appointment')]
    for items in appointments:
        print 'Dear {}, \nI look forward to meeting with you on {}.\nBEST, \nMe' \
    .format(client_name, appointment)
        return
    
