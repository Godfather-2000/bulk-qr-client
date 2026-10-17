# src/bulkqr/client.py

import requests
from typing import List, Dict, Any
from .exceptions import (
    InvalidAPIKeyError, 
    OutOfCreditsError, 
    NotFoundError,
    InvalidInputError,
    RateLimitError,
    ServiceBusyError, 
    InternalServerError,
    BulkQRError
)

class BulkQRClient:
    def __init__(self, api_key: str, base_url: str = "https://bulk-qr-api.onrender.com"):
        """
        Initialize the BulkQR client.
        
        Args:
            api_key (str): Your secret or trial API key.
            base_url (str): The production root URL of your FastAPI backend on Render.
        """
        if not api_key or not isinstance(api_key, str):
            raise ValueError("A valid API key string must be provided.")
            
        self.api_key = api_key.strip()
        self.base_url = base_url.rstrip("/")

    def generate_labels(self, items: List[Dict[str, Any]], output_file: str = "labels.pdf") -> None:
        """
        Sends items to the API and saves the returned PDF file locally.
        
        Args:
            items (list): A list of dictionaries containing your QR data and labels.
            output_file (str): The filename/path where the PDF should be saved.
        """
        url = f"{self.base_url}/api/v1/generate-labels"
        
        headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }
        
        payload = {"items": items}

        try:
            # stream=True handles binary streaming efficiently.
            # timeout=(5, 60): 5 seconds to connect, 60 seconds to receive data (prevents infinite hanging).
            response = requests.post(
                url, 
                json=payload, 
                headers=headers, 
                stream=True, 
                timeout=(5.0, 60.0)
            )
            
            # Map HTTP status codes to clean Python exceptions
            status = response.status_code
            
            if status == 401:
                raise InvalidAPIKeyError("Invalid or missing API key. Check your key and try again.")
            elif status == 402:
                raise OutOfCreditsError("Your account has run out of credits. Please contact support.")
            elif status == 404:
                raise NotFoundError(f"API endpoint not found at {url}. Check your base URL.")
            elif status == 422:
                raise InvalidInputError(f"Malformed or invalid input data: {response.text}")
            elif status == 429:
                raise RateLimitError("Rate limit exceeded. Please slow down your requests.")
            elif status == 503:
                raise ServiceBusyError("Server is currently busy handling other requests. Please try again shortly.")
            elif 500 <= status < 600:
                raise InternalServerError(f"Server error ({status}): {response.text}")
            elif status != 200:
                raise BulkQRError(f"Unexpected error ({status}): {response.text}")

            # Write binary stream directly to a local PDF file safely using a context manager.
            # Even if an interruption occurs mid-stream, the file descriptor closes cleanly.
            with open(output_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        
        except requests.exceptions.Timeout:
            raise BulkQRError("The request timed out. The server took too long to respond.")
        except requests.exceptions.ConnectionError:
            raise BulkQRError("Failed to connect to the BulkQR server. Check your network connection or base URL.")
        except requests.exceptions.RequestException as e:
            raise BulkQRError(f"Network error connecting to BulkQR API: {e}")