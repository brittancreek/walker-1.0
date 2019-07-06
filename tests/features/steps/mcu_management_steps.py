'''
mcu_management_steps.py

Copyright © Brittan Creek
'''
from behave import *

import pathlib

@given(u'an mcu')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an mcu')


@when(u'the mcu is powered up')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the mcu is powered up')

@then(u'I can verify a production mcu')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can verify a production mcu')

@given(u'a production mcu')
def step_impl(context):
    context.bootfile = pathlib.Path('features/steps/source/boot.py')

@when(u'power is applied')
def step_impl(context):
    context.mainfile = pathlib.Path('features/steps/source/main.py')

@then(u'the mcu should boot up to default state')
def step_impl(context):
    assert context.bootfile.exists(), "Error: Missing boot.py file."
    assert context.mainfile.exists(), "Error: Missing main.py file."
