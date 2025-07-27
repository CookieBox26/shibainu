# shibainu

### Installation

For **Linux with CUDA 12.4** or **Windows with CPU**, you can install dependencies using [uv](https://github.com/astral-sh/uv):

```
pip install uv
uv sync
```

If you're on a different OS/CUDA, edit `pyproject.toml`, delete `uv.lock`, and run the commands above.

If you're unable to use uv, install the dependencies from `pyproject.toml` manually.

### Execution Commands

```
uv run python run.py
```
