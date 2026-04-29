"""FastMCP - A fast, Pythonic interface for the Model Context Protocol.

This is a fork of PrefectHQ/fastmcp with additional features and improvements.
"""

from fastmcp.server import FastMCP
from fastmcp.tools import tool
from fastmcp.resources import resource
from fastmcp.prompts import prompt
from fastmcp.context import Context
from fastmcp.exceptions import FastMCPError, ToolError, ResourceError

__version__ = "0.1.0"
__all__ = [
    "FastMCP",
    "tool",
    "resource",
    "prompt",
    "Context",
    "FastMCPError",
    "ToolError",
    "ResourceError",
]
