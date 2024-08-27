import argparse

from picoplugin.cmds import cmd_init, cmd_new
from picoplugin.config import PluginConfig

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(required=True)

# init plugin
init_parser = subparser.add_parser('init')
init_parser.add_argument('name', type=str, default="example")
init_parser.set_defaults(func=cmd_init)

# new plugin
new_parser = subparser.add_parser('new')
new_parser.add_argument('name', type=str, default="example")
new_parser.set_defaults(func=cmd_new)


def main():
    args = parser.parse_args()
    args = vars(args)
    call = args.pop("func")
    call(PluginConfig(**args))


if __name__ == "__main__":
    main()
