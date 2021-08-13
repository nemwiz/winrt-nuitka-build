### Minimal reproduction of building winrt library with Nuitka

### Setup

Run `pip install -r requirements.txt`

### Steps to reproduce

- Build with Nuitka `python -m nuitka --standalone --enable-plugin=anti-bloat --noinclude-pytest-mode=nofollow --noinclude-setuptools-mode=nofollow main.py`
- Open command line, `cd` into this folder and run `start "test" call main.dist\main.exe`
- You should see `LowLevelDevicesAggregateProvider` error