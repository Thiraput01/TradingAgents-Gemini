# TradingAgents (But for Gemini)

This repository is a fork of [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) and has been adapted to use Google Gemini environments instead of OpenAI.

For detailed information about the TradingAgents framework, its architecture, and advanced usage, please refer to the [original repository](https://github.com/TauricResearch/TradingAgents).

## Installation and CLI

### Installation

Clone this repository:
```bash
git clone https://github.com/your-username/TradingAgents.git # Replace with your repository URL
cd TradingAgents
```

Create a virtual environment using Conda:
```bash
conda create -n tradingagents python=3.13
conda activate tradingagents
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Required APIs

You will need the FinnHub API for financial data. All of our code is implemented with the free tier.
```bash
export ALPHA_VANTAGE_API_KEY=$ALPHA_VANTAGE_API_KEY
```

You will need the Google API for all the agents.
```bash
export GOOGLE_API_KEY=$YOUR_GOOGLE_API_KEY
```

### CLI Usage

You can try out the CLI directly by running:
```bash
python -m cli.main
```
You will see a screen where you can select your desired tickers, date, LLMs, research depth, etc.
