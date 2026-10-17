# BulkQR Python SDK (`bulk-qr-client`)

A lightweight, production-ready Python SDK for generating print-ready bulk QR code sheets and PDF labels via API.

## Quickstart

### 1. Installation
Install the package using pip:
```python
pip install bulk-qr-client
```
### 2. Generate Labels
Here is how simple it is to generate and save a professional label PDF directly from your Python script:
```python
from bulkqr import BulkQRClient
from bulkqr.exceptions import (
    BulkQRError,
    InvalidAPIKeyError,
    OutOfCreditsError,
    RateLimitError,
    ServiceBusyError
)

# Initialize the client with your API key
client = BulkQRClient(api_key="your_api_key_here")

# Define items to include in the QR generation request
items = [
    {"data": "https://example.com/item/001", "label": "SKU-001: Widget A"},
    {"data": "https://example.com/item/002", "label": "SKU-002: Widget B"},
]

try:
    # Generate and save the PDF locally
    client.generate_labels(items=items, output_file="inventory_labels.pdf")
    print("PDF generated successfully and saved as 'inventory_labels.pdf'!")

except InvalidAPIKeyError:
    print("Error: Invalid or missing API key.")
except OutOfCreditsError:
    print("Error: You have run out of credits. Please top up your account.")
except RateLimitError:
    print("Error: Rate limit exceeded. Please slow down your requests.")
except ServiceBusyError:
    print("Error: Server is currently busy handling other requests. Try again shortly.")
except BulkQRError as e:
    # Catches network timeouts, disconnections, or general client errors
    print(f"SDK/Network Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```


## 🛡️ Error Handling
bulk-qr-client maps API responses and network conditions directly to clean, descriptive Python exceptions so you can handle failures gracefully in production environments:

`InvalidAPIKeyError` (`HTTP 401`): Provided API key is invalid or missing.

`OutOfCreditsError` (`HTTP 402`): Account has exhausted available credits.

`NotFoundError` (`HTTP 404`): Endpoint path or resource was not found.

`InvalidInputError` (`HTTP 422`): Malformed payload or input formatting issue.

`RateLimitError` (`HTTP 429`): Request rate limit exceeded.

`ServiceBusyError` (`HTTP 503`): Service is busy handling other concurrent requests.

`InternalServerError` (`HTTP 500-599`): Unhandled server error.

`BulkQRError`: Base exception class; also raised for network disconnections or when the server takes too long to respond (timeout).

## 🔑 Getting an API Key

To request a trial API key with test credits included, open an issue in this repository or contact support.

## ⚖️ License
Distributed under the `MIT License`. See `LICENSE` for details.
