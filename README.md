# fragrantauto-utils

A lightweight Python toolkit designed for automated interaction with decentralized exchange protocols and liquidity pools. It provides robust abstractions for transaction orchestration, price monitoring, and data parsing across EVM-compatible chains.

## Features

*   **Gas-Optimized Transaction Dispatcher**: Automated fee estimation and nonce management to minimize failed transactions during high network congestion.
*   **Real-time Liquidity Tracking**: High-performance streaming interface for monitoring pool reserves and price slippage via WebSocket providers.
*   **Smart Contract Interaction Layer**: Simplified ABI handling for common DeFi primitives, supporting batching of swaps and multi-hop liquidity routing.
*   **Exception Resiliency**: Built-in retry logic and circuit breakers for handling node RPC timeouts and transient chain reorganizations.

## Installation

Install the package via `pip` directly from the repository:

```bash
pip install git+https://github.com/Developer/fragrantauto-utils.git
```

Ensure you have your environment variables configured for your preferred RPC provider:

```bash
export RPC_URL="https://mainnet.infura.io/v3/YOUR_PROJECT_ID"
export PRIVATE_KEY="your_wallet_private_key"
```

## Basic Usage

The following example demonstrates how to initialize the swap client and execute a token exchange:

```python
from fragrantauto import SwapClient

# Initialize client
client = SwapClient(rpc_url="RPC_URL", private_key="PRIVATE_KEY")

# Execute a swap of 1.0 ETH for DAI
tx_hash = client.swap(
    token_in="ETH",
    token_out="DAI",
    amount=1.0,
    slippage=0.5
)

print(f"Transaction successful: {tx_hash}")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.