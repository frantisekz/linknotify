#!/usr/bin/python3

import argparse
import sys


def _run_server(args):
    from linknotify import linknotify_server
    print("running server")
    linknotify_server.app.run(host="0.0.0.0")

def _run_client(args):
    from linknotify import linknotify_client
    print("running client")
    linknotify_client.main()


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(title="Server or client", help=" --help")

    server = subparser.add_parser("server", help="run in server mode")
    server.set_defaults(func=_run_server)

    client = subparser.add_parser("client", help="run in client mode")
    client.set_defaults(func=_run_client)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        # If no cmdline args were provided, func is missing
        # https://bugs.python.org/issue16308
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()