import argparse

from picoplugin.cmds import cmd_init, cmd_new
from picoplugin.config import PluginConfig

parser = argparse.ArgumentParser(
    prog='picoplugin',
    description='Tool for generating picodata plugins',
)
subparser = parser.add_subparsers(required=True)

# init plugin
init_parser = subparser.add_parser('init')
init_parser.set_defaults(cmd_name='init')
init_parser.set_defaults(func=cmd_init)

# new plugin
new_parser = subparser.add_parser('new')
new_parser.add_argument('name', type=str, default="example")
new_parser.set_defaults(cmd_name='new')
new_parser.set_defaults(func=cmd_new)


def main():
    args = parser.parse_args()
    args = vars(args)
    call = args.pop("func")
    cfg = PluginConfig(**args)
    call(cfg)


if __name__ == "__main__":
    main()
