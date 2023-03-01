import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser(...)
    parser.add_argument("-stocks")
    return parser.parse_args(args)


def main(args=sys.argv[1:]):
    parsed_args = parse_args(args)
    print(parsed_args.stocks)


if __name__ == "__main__":
    main()


def test_main(capsys):
    main(["-stocks", "tsla"])
    stdout, stderr = capsys.readouterr()
    assert stdout == "tsla\n"
