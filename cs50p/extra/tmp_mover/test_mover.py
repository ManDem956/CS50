from pathlib import Path
import shutil  # noqa: F401
import pytest
from mover import sort_by_extension

TEST_FILE_NAME = "test_{id}{ext}"


@pytest.fixture
def setup_data(request):
    path = request.param["path"]
    extensions = tuple(request.param["data_files"]) + request.param["extra_files"]
    Path(path).mkdir(parents=True, exist_ok=True)
    for id in range(request.param["count"]):
        for ext in extensions:
            Path(path, TEST_FILE_NAME.format(id=id, ext=ext)).touch()
    data = path, request.param["data_files"]
    yield data
    # shutil.rmtree(path)  # uncomment it to cleanup after test finishes.


@pytest.mark.parametrize(
    "setup_data, expected",
    [
        (  # one test setup - start
            {
                "path": "source",
                "count": 5,
                "data_files": {
                    ".txt": "text_files",
                    ".csv": "text_files",
                    ".zip": "archive_files",
                },
                "extra_files": (".db",),
            },
            [Path("source/text_files"), Path("source/archive_files")],
        ),  # one test setup
        (  # another test setup - start
            {
                "path": "source",
                "count": 30,
                "data_files": {".doc": "Documents", ".mov": "Video", ".mp3": "Audio"},
                "extra_files": (".gardage",),
            },
            [
                Path("source/Documents"),
                Path("source/Video"),
                Path("source/Audio"),
            ],
        ),  # another test setup
    ],
    indirect=["setup_data"],
)
def test_sort_by_extension(setup_data, expected):
    sort_by_extension(*setup_data)
    path = Path(setup_data[0])
    dirs = [item for item in path.iterdir() if item.is_dir()]
    assert sorted(expected) == sorted(dirs)
