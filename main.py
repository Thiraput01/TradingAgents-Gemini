from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "google"
config["backend_url"] = "https://generativelanguage.googleapis.com/v1"
config["deep_think_llm"] = "gemini-2.0-flash-exp"
config["quick_think_llm"] = "gemini-2.0-flash-exp"
config["max_debate_rounds"] = 1
config["online_tools"] = True

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
