"""FastMCP - A fast, Pythonic interface for the Model Context Protocol.

This is a fork of PrefectHQ/fastmcp with additional features and improvements.

Fork notes:
- Tracking upstream: https://github.com/PrefectHQ/fastmcp
- Added PromptError to public exceptions for consistency with ToolError/ResourceError
- Exposed __version__ in __all__ for easier introspection
- Added __author__ for personal fork identification
- Added convenience import of NotFoundError for cleaner error handling in user code
"""

from fastmcp.server import FastMCP
from fastmcp.tools import tool
from fastmcp.resources import resource
from fastmcp.prompts import prompt
from fastmcp.context import Context
from fastmcp.exceptions import FastMCPError, ToolError, ResourceError, PromptError, NotFoundError

__version__ = "0.1.0"
__author__ = "personal fork"
__all__ = [
    "FastMCP",
    "tool",
    "resource",
    "prompt",
    "Context",
    "FastMCPError",
    "ToolError",
    "ResourceError",
    "PromptError",
    "NotFoundError",
    "__version__",
    "__author__",
]
