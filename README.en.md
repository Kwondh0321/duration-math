# duration-math

[한국어](README.md)

Parse and add human-friendly durations such as 1h30m.

A small, dependency-free Python command-line tool that does one job well:
**calculate durations**.

## Highlights

- Focused CLI with predictable text output
- Python standard library only at runtime
- Importable core functions for reuse in scripts
- Unit tests and GitHub Actions CI

## Requirements

Python 3.11 or newer.

## Install

~~~bash
git clone https://github.com/Kwondh0321/duration-math.git
cd duration-math
python -m pip install .
~~~

For an isolated command-line installation, pipx install . also works.

## Quick start

~~~bash
duration-math 1h30m 45m -10s
~~~

Run duration-math --help for every option.

## Development

~~~bash
python -m unittest discover -s tests -v
python duration_math.py --help
~~~

## Scope

This repository intentionally stays small. It favors transparent behavior,
standard formats, and composability with shell pipelines over a large
dependency tree or an interactive interface.

## License

MIT
