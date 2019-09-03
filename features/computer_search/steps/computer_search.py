# -*- coding: UTF-8 -*-

import logging
import requests
import json

class ComputerSearch(object):
    def __init__(self):
        self.name  = None
        self.result = None

    def search_term(self, name):
        self.name = name

    def go(self):
        response = requests.get("http://localhost:8001/api/ListIds?name="+self.name)
        strIds = json.loads(response.text)
        strIds = list(map(lambda x: int(x), strIds))
        self.result = strIds
        # logging.warning(response.text)


# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import *

@given('I use "{name}" as the computer name')
def step_impl(context, name):
    context.computer_search = ComputerSearch()
    context.computer_search.search_term(name)

@when('I execute the search')
def step_impl(context):
    context.computer_search.go()

@then('it should list {computer_ids:IdList}')
def step_impl(context, computer_ids):
    # logging.warning(context.computer_search.result)
    # logging.warning(type(context.computer_search.result))
    assert_that(context.computer_search.result, equal_to(computer_ids))


@given('I use orange as the computer name2')
def step_impl(context):
    context.computer_search = ComputerSearch()
    context.computer_search.search_term("orange")

@when('I execute the search2')
def step_impl(context):
    context.computer_search.go()

@then('it should list2 {computer_ids:IdList}')
def step_impl(context, computer_ids):
    # logging.warning(context.computer_search.result)
    # logging.warning(type(context.computer_search.result))
    assert_that(context.computer_search.result, equal_to(computer_ids))





