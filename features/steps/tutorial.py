from behave import *

@given('I am a guest user')
def step_impl(context):
    pass

@when('I access the app page')
def step_impl(context):
    assert True is not False

@then('I will see all elements in page')
def step_impl(context):
    assert context.failed is False