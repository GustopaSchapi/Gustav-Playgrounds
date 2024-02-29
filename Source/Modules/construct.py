from os import environ


def main(str_to_fmt: str) -> str:
    str_fmt = f"\n{str_to_fmt.lower()}"
    str_fmt += f"\n{environ.get('PATH')}"
    return str_fmt
