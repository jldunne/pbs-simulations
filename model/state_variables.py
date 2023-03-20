from dataclasses import dataclass
from datetime import datetime


@dataclass
class StateVariables:
    """State Variables
    Each State Variable is defined as:
    state variable key: state variable type = default state variable value
    """
    timestamp: datetime = None

