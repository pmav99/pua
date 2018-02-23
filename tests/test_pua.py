# -*- coding: utf-8 -*-

import random

import pytest
from click.testing import CliRunner

from pua import get_ua, get_header, USER_AGENTS
from pua.cli import main


def test_cli_error_code():
    # The CLI must return no errors
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0


@pytest.mark.parametrize('seed', [0, 23, 42242, 234132131])
def test_cli_code_equal(seed):
    # if we reseed the random generator,
    # the output of the CLI and the code should be the same
    random.seed(seed)
    runner = CliRunner()
    result = runner.invoke(main, [])
    cli_ua = result.output.strip()
    #
    random.seed(seed)
    code_ua = get_ua()
    assert cli_ua == code_ua


def test_get_header():
    header = get_header()
    assert isinstance(header, dict)
    assert "User-Agent" in header
    assert header["User-Agent"] in USER_AGENTS
