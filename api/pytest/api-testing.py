
# ----- Documentation -----
# - Run this test using: pytest todo-app-test.py
# - APIRequestContext -> https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-post
# - Python F Strings -> https://realpython.com/python-f-strings/https://realpython.com/python-f-strings/
# - Pytest Fixtures -> https://playwright.dev/python/docs/test-runners#fixtures
# - Python Function Annotations -> https://peps.python.org/pep-3107/
# - Typing: https://docs.python.org/3/library/typing.html
# -------------------------

# This module provides runtime support for type hints.
from typing import Generator
# This module imports pytest
import pytest
# This module import instances and modules required by playwright
from playwright.sync_api import Playwright, APIRequestContext, expect
# https://stackoverflow.com/questions/64559985/pytest-how-to-pass-parameters-data-between-tests

# Define fixtures for static data used by tests.
# This data can be accessed by all tests in the suite unless specified otherwise.
# This could be data as well as helpers of modules which will be passed to all tests.

# Send this fixture as parameter in your tests. we can also use the conftest.py


@pytest.fixture(scope="module")
def myIds():
    # keys list
    keys = []
    yield keys

# In testing, a fixture provides a defined, reliable and consistent context for the tests.
# We may configure "FUNCTION" scope & "SESSION" scope.


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
    # class typing.Generator
    # It means that you need to declare types of variables, parameters, and return values_
    # of a function upfront. The predefined types allow the compilers to check the code before
    # compiling and running the program.
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    # This method discards all stored responses
    request_context.dispose()


def test_post_todo(api_request_context: APIRequestContext, myIds) -> None:
    # https://www.w3schools.com/python/python_dictionaries.asp
    data = {
        "completed": False,
        "title": "test from playwright",
        "id": "500",
    }
    new_todo = api_request_context.post(
        f"/todos", data=data
    )
    assert new_todo.ok

    todos_response = new_todo.json()
    # In order to check the logs, add -s as part of the command.
    print("")
    print(f"New Todo request: {new_todo}")
    print(f"todo_response Var: {todos_response}")
    # print(f"todo_response Var: {todos_response['id']}")

    myIds.append(todos_response['id'])


def test_get_todo(api_request_context: APIRequestContext, myIds) -> None:
    get_todo = api_request_context.get(
        f"/todos/{myIds[0]}"
    )
    assert get_todo.ok

    response = get_todo.json()

    assert response['title'] == "test from playwright"
    assert response['completed'] == False

    print(f"Get todo request: {get_todo}")
    print(f"Response: {response}")


def test_update_todo(api_request_context: APIRequestContext, myIds) -> None:
    data = {
        "completed": True
    }
    patch_todo = api_request_context.patch(
        f"/todos/{myIds[0]}", data=data
    )
    assert patch_todo.ok

    response = patch_todo.json()

    assert response['title'] == "test from playwright"
    assert response['completed'] == True

    print(f"Update todo request: {patch_todo}")
    print(f"Response: {response}")


# @pytest.mark.skip(reason="Just for demo purposes")
def test_delete_todo(api_request_context: APIRequestContext, myIds) -> None:
    delete_todo = api_request_context.delete(
        f"/todos/{myIds[0]}"
    )
    assert delete_todo.ok

    response = delete_todo.json()

    print(f"Delete todo request: {delete_todo}")
    print(f"Response: {response}")
