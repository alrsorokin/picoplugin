from dataclasses import dataclass, field


@dataclass
class ServiceConfig:
    name: str = field(default="example")
    description: str = field(
        default="this is an example service for picodata plugin")
    default_config: dict = field(default_factory=lambda: {})
