from dataclasses import dataclass, field
from .service import ServiceConfig


@dataclass
class PluginConfig:
    name: str = field(default="example")
    description: str = field(
        default="this is an example plugin for picodata")

    services: list = field(default_factory=lambda: [ServiceConfig])
    path: str = field(default="")
