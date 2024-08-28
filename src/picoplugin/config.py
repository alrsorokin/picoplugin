import os
from dataclasses import dataclass, field


@dataclass
class ServiceConfig:
    name: str = field(default="example")
    description: str = field(
        default="this is an example service for picodata plugin")
    default_config: dict = field(default_factory=lambda: {})


@dataclass
class PluginConfig:
    cmd_name: str = field()
    name: str = field(default=os.path.basename(os.getcwd()))
    description: str = field(
        default="this is an example plugin for picodata")

    services: list = field(default_factory=lambda: [ServiceConfig])
    path: str = field(default=os.getcwd())

    def __post_init__(self):
        if self.cmd_name == "new":
            self.path = os.path.join(self.path, self.name)
