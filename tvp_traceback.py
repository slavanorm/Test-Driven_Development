"""
tvp-traceback

replaces sys.excepthook

"""

import sys
import traceback


lets_trace_this = True


def tb_on(tb):
    gl = tb.tb_frame.f_globals
    return "lets_trace_this" in gl


def tb_levels(tb):
    length = 0
    while tb and tb_on(tb):
        tb = tb.tb_next
        length += 1
    return length


def ttb(type, value, tb):
    length = tb_levels(tb)
    print(
        "".join(
            traceback.format_exception(type, value, tb, length)
        )
    )


sys.excepthook = ttb
