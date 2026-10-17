# src/bulk-qr/exceptions.py

class BulkQRError(Exception):
    """Base exception for all BulkQR errors."""
    pass

class InvalidAPIKeyError(BulkQRError):
    """Raised when the API key is invalid, missing, or unauthorized (HTTP 401)."""
    pass

class OutOfCreditsError(BulkQRError):
    """Raised when the account has run out of credits (HTTP 402)."""
    pass

class NotFoundError(BulkQRError):
    """Raised when the requested endpoint cannot be found (HTTP 404)."""
    pass

class InvalidInputError(BulkQRError):
    """Raised when the input payload is malformed or invalid (HTTP 422)."""
    pass

class RateLimitError(BulkQRError):
    """Raised when the client has sent too many requests too quickly (HTTP 429)."""
    pass

class ServiceBusyError(BulkQRError):
    """Raised when the server's CPU semaphore blocks the request due to heavy load (HTTP 503)."""
    pass

class InternalServerError(BulkQRError):
    """Raised when the server encounters an unexpected internal error (HTTP 500-599)."""
    pass