# fragrantauto-utils

`fragrantauto-utils` is a high-performance Python toolkit designed for automated crypto trading and decentralized protocol interaction. It provides streamlined abstractions for managing wallet state, executing on-chain swaps, and monitoring liquidity pools.

## Features

*   **Async Web3 Wrappers:** Optimized `web3.py` boilerplate to handle high-frequency transaction signing and gas estimation without blocking the event loop.
*   **Decentralized Exchange (DEX) Router:** Native support for Uniswap V3 and PancakeSwap routing, including automatic slippage calculation and path optimization.
*   **On-Chain Monitoring:** Lightweight listeners for tracking event logs (Transfer, Swap, Mint) across EVM-compatible networks with minimal latency.
*   **Portfolio Reconciliation:** Automated balance tracking and token decimal normalization across multiple chains using a single, unified interface.

## Installation

Ensure you have Python 3.10+ installed. Install the package directly via pip:

```bash
pip install fragrantauto-utils
```

For local development or to utilize the latest features:

```bash
git clone https://github.com/Developer/fragrantauto-utils.git
cd fragrantauto-utils
pip install -r requirements.txt
python setup.py install
```

## Basic Usage

The following example demonstrates how to initialize a wallet provider and query a token balance on the Ethereum mainnet.

```python
from fragrantauto.provider import Web3Provider
from fragrantauto.utils import format_balance

# Initialize the provider
w3 = Web3Provider(rpc_url="https://eth.llamarpc.com")

# Get wallet balance for a target contract
balance = w3.get_balance("0x742d35Cc6634C0532925a3b844Bc454e4438f44e")
print(f"Current Balance: {format_balance(balance)} ETH")
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.