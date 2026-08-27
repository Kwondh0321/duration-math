"""Parse and add human-friendly durations such as 1h30m."""

import argparse
import re

UNITS = {"d": 86400, "h": 3600, "m": 60, "s": 1}
TOKEN = re.compile(r"([+-]?\d+(?:\.\d+)?)([dhms])")

def parse_duration(value):
    compact = value.replace(" ", "")
    matches = list(TOKEN.finditer(compact))
    if not matches or "".join(m.group(0) for m in matches) != compact:
        raise ValueError(f"invalid duration: {value}")
    return sum(float(match.group(1)) * UNITS[match.group(2)] for match in matches)

def format_duration(seconds):
    sign = "-" if seconds < 0 else ""
    remaining = int(round(abs(seconds)))
    parts = []
    for suffix, size in UNITS.items():
        value, remaining = divmod(remaining, size)
        if value:
            parts.append(f"{value}{suffix}")
    return sign + ("".join(parts) or "0s")

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("durations", nargs="+")
    args = parser.parse_args(argv)
    try:
        total = sum(parse_duration(x) for x in args.durations)
    except ValueError as error:
        parser.error(str(error))
    print(format_duration(total))

if __name__ == "__main__":
    main()
