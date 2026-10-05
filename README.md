# fragrantauto-utils

`fragrantauto-utils` is a high-performance Python toolkit designed for automated cryptocurrency trading strategy development and portfolio management. It provides streamlined interfaces for executing complex order types and tracking real-time market data across multiple decentralized exchanges.

### Features

*   **Async Order Execution:** Non-blocking API wrappers for rapid order routing and management, minimizing slippage during high-volatility events.
*   **Arbitrage Monitoring:** Native utilities to track spread differentials between liquidity pools with sub-millisecond latency.
*   **Data Normalization:** Robust serialization methods to convert diverse exchange websocket streams into a unified internal schema.
*   **Risk Guardrails:** Pre-built validation logic to enforce circuit breakers, position sizing constraints, and automated emergency liquidations.

### Installation

Requires Python 3.9 or higher. Install the package via pip:

```bash
pip install fragrantauto-utils
```

For development mode with testing dependencies:

```bash
git clone https://github.com/developer/fragrantauto-utils.git
cd fragrantauto-utils
pip install -e .[dev]
```

### Usage

Initialize the client and execute a basic market buy order using the utility wrapper:

```python
from fragrantauto import Client

# Initialize with API credentials
client = Client(api_key="your_key", secret="your_secret")

# Execute a market buy order for 0.5 ETH/USDT
order = client.trade.market_buy(
    symbol="ETHUSDT",
    quantity=0.5,
    test_mode=True
)

print(f"Order executed successfully: {order['order_id']}")
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Disclaimer: This tool is for educational purposes. Use at your own risk. The author is not responsible for financial losses incurred through automated trading.*