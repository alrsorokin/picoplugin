import os
import subprocess
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 'templates')),
    autoescape=select_autoescape()
)
env.globals['service_name'] = lambda service: f"{service.name.capitalize()}Service"
env.globals['service_cfg_name'] = lambda service: f"{service.name.capitalize()}ServiceCfg"


def generate_manifest(cfg):
    template = env.get_template("manifest.yaml.j2")
    template.stream(cfg=cfg).dump(os.path.join(cfg.path, "manifest.yaml"))


def generate_dependencies(cfg):
    # todo: get picoplugin version from crates.io
    picoplugin = 'git = "ssh://git@git.picodata.io/picodata/picodata/picodata.git", rev = "25264bc35e4dd3a83d1aecbe006f332e8b9517e5"'
    template = env.get_template("cargo.toml.j2")
    template.stream(cfg=cfg, picoplugin=picoplugin).dump(
        os.path.join(cfg.path, "Cargo.toml"))


def generate_services(cfg):
    template = env.get_template("service.rs.j2")
    for service in cfg.services:
        service_dir = os.path.join(cfg.path, "src", service.name)
        if not os.path.exists(service_dir):
            os.makedirs(service_dir)
        service_mod = os.path.join(service_dir, "mod.rs")
        template.stream(service=service).dump(service_mod)


def registry_services(cfg):
    template = env.get_template("lib.rs.j2")
    template.stream(cfg=cfg).dump(os.path.join(cfg.path, "src", "lib.rs"))


def template(cargo_cmd):
    def generate(cfg):
        try:
            cargo_cmd(cfg)
            generate_dependencies(cfg)
            generate_manifest(cfg)
            generate_services(cfg)
            registry_services(cfg)
        except Exception as exc:
            print(f"Plugin generation error: {repr(exc)}")
    return generate


@template
def cmd_init(args):
    subprocess.run(["cargo", "init", "--lib", "--name", args.name], check=True)


@template
def cmd_new(args):
    subprocess.run(["cargo", "new", "--lib", args.name], check=True)
