# shibainu

### Installing dependencies

For **Linux with CUDA 12.4** or **Windows with CPU**, you can install dependencies using [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
# Example: install uv on Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Example: install uv on Windows
pip install uv

# Check version (tested with uv 0.8.3)
uv --version  # e.g. uv 0.8.3

# Install dependencies
uv sync
```

If your setup is different, edit `pyproject.toml`, delete `uv.lock`, and run the commands above.

If you're unable to use uv, install the dependencies from `pyproject.toml` manually.

### Running commands

```
uv run python run.py
```
