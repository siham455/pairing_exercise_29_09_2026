from lib.user_story import *


def test_list_not_empty():
    result = user_story([])
    assert result == ''

def test_user_story_returns_name():
    result = user_story(["Bart"])
    assert result == 'Bart'

def test_user_story_returns_two_names():
    result = user_story(["Bart", "Lisa"])
    assert result == 'Bart & Lisa'

def test_user_story_returns_over_two_names():
    result = user_story(["Bart", "Lisa", "Maggie"])
    assert result == 'Bart, Lisa & Maggie'