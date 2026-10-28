# fragrantauto-utils

`fragrantauto-utils` is a lightweight Python toolkit designed to streamline automated crypto trading operations and portfolio management. It provides high-performance wrappers for common exchange API tasks and robust error handling for volatile market conditions.

### Features

*   **Rate-Limit Aware Client:** Built-in decorator patterns to automatically handle exchange API rate limits and prevent socket timeouts.
*   **Order Lifecycle Management:** Simplified interface for placing complex limit/stop-loss orders with automated state tracking.
*   **Data Normalization:** Converts heterogeneous raw API responses from multiple exchanges into a unified, standardized schema for seamless backtesting.
*   **Websocket Stream Handler:** Asynchronous event loop support for real-time order book monitoring and latency-sensitive execution.

### Installation

Ensure you have Python 3.9+ installed. You can install the package directly via pip:

```bash
pip install fragrantauto-utils
```

For local development or custom modifications:

```bash
git clone https://github.com/Developer/fragrantauto-utils.git
cd fragrantauto-utils
pip install -r requirements.txt
python setup.py install
```

### Basic Usage

Below is a quick example of how to initialize a client and fetch the current mid-market price for a specific pair.

```python
from fragrantauto.client import CryptoClient

# Initialize with API credentials
client = CryptoClient(api_key='YOUR_API_KEY', secret='YOUR_SECRET')

# Fetch real-time market data
ticker = client.get_ticker("BTC-USDT")

print(f"Current Price: {ticker['ask']}")

# Execute a market order
order = client.place_market_order(
    pair="BTC-USDT",
    side="buy",
    amount=0.01
)
print(f"Order executed: {order['id']}")
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.