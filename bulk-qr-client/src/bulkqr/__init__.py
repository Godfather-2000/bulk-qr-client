# src/bulk-qr/__init__.py

from .client import BulkQRClient
from .exceptions import (
    BulkQRError,
    InvalidAPIKeyError,
    OutOfCreditsError,
    NotFoundError,
    InvalidInputError,
    RateLimitError,
    ServiceBusyError,
    InternalServerError,
)

__version__ = "0.1.0"

__all__ = [
    "BulkQRClient",
    "BulkQRError",
    "InvalidAPIKeyError",
    "OutOfCreditsError",
    "NotFoundError",
    "InvalidInputError",
    "RateLimitError",
    "ServiceBusyError",
    "InternalServerError",
]