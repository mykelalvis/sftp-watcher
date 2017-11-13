import pytest
from click.testing import CliRunner
from sftpwatcher import watch
import shutil
import os
import os.path


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if os.path.exists(directory):
        shutil.rmtree(file_path, True)
    shutil.copytree('src/test/resources/', file_path)
    return directory


@pytest.fixture
def runner():
    ensure_dir('./target')
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(watch.main)
    assert result.exit_code == 2
    assert result.exception
    assert 'Error: Missing argument' in str(result.output)


def test_cli_bad_path(runner):
    result = runner.invoke(watch.main, ['X'])
    assert result.exit_code == 2
    assert result.exception
    assert 'Invalid value for "path": Path "X" does not exist' in str(result.output)


def test_cli_good_path(runner):
    result = runner.invoke(watch.main, ['./target/watchdir'])
    assert result.exit_code == 0
    assert 'echo is not necessarily' in str(result.output)


def test_cli_good_path_matching(runner):
    result = runner.invoke(watch.main, ['--debug', '--matches', '.*txt', './target/watchdir'])
    assert result.exit_code == 0
    assert 'tempfile.txt' in str(result.output)


def test_cli_good_path_relocate(runner):
    result = runner.invoke(watch.main,
                           ['--debug', '--relocate', './target/relo', '--matches', '.*txt', './target/watchdir'])
    assert result.exit_code == 0
    assert 'after relocating to' in str(result.output)


def test_cli_good_path_relocate_none(runner):
    result = runner.invoke(watch.main, ['--debug', '--relocate', 'target/relo', '--matches', '.*md', 'target/watchdir'])
    assert result.exit_code == 0
    assert 'after relocating to' not in str(result.output)
