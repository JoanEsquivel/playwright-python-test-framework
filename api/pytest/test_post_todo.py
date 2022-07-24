
#----- Documentation -----
#- Run this test using: pytest todo-app-test.py
#- APIRequestContext -> https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-post
#- Python F Strings -> https://realpython.com/python-f-strings/https://realpython.com/python-f-strings/
#- Pytest Fixtures -> https://playwright.dev/python/docs/test-runners#fixtures
#- Python Function Annotations -> https://peps.python.org/pep-3107/
#- Typing: https://docs.python.org/3/library/typing.html
#-------------------------

#This module provides runtime support for type hints.
from typing import Generator
#This module imports pytest
import pytest
#This module import instances and modules required by playwright
from playwright.sync_api import Playwright, Page, APIRequestContext, expect


#In testing, a fixture provides a defined, reliable and consistent context for the tests.
#We may configure "FUNCTION" scope & "SESSION" scope.
@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
    #class typing.Generator
    #It means that you need to declare types of variables, parameters, and return values_
    # of a function upfront. The predefined types allow the compilers to check the code before
    # compiling and running the program.
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    #This method discards all stored responses
    request_context.dispose()


def test_post_todo(api_request_context: APIRequestContext) -> None:
    #https://www.w3schools.com/python/python_dictionaries.asp
    data = {
        "completed": False,
        "title": "test",
        "id": "500",
    }
    new_todo = api_request_context.post(
        f"/todos", data=data
    )
    assert new_todo.ok

    todos_response = new_todo.json()
    #In order to check the logs, add -s as part of the command.
    print("")
    print(f"todo Var: {new_todo}")
    print(f"todo_response Var: {todos_response}")


    







    