╭──────────────────────────────────────────────── Traceback (most recent call last) ─────────────────────────────────────────────────╮
│ /home/impen/workspace/playground/TradingAgents/cli/main.py:1123 in analyze │
│ │
│ 1120 │
│ 1121 @app.command() │
│ 1122 def analyze(): │
│ ❱ 1123 │ run_analysis() │
│ 1124 │
│ 1125 │
│ 1126 if **name** == "**main**": │
│ │
│ /home/impen/workspace/playground/TradingAgents/cli/main.py:753 in run_analysis │
│ │
│ 750 │ config["llm_provider"] = selections["llm_provider"].lower() │
│ 751 │ │
│ 752 │ # Initialize the graph │
│ ❱ 753 │ graph = TradingAgentsGraph( │
│ 754 │ │ [analyst.value for analyst in selections["analysts"]], config=config, debug=True │
│ 755 │ ) │
│ 756 │
│ │
│ ╭───────────────────────────────────────────────────────── locals ─────────────────────────────────────────────────────────╮ │
│ │ config = { │ │
│ │ │ 'project_dir': '/home/impen/workspace/playground/TradingAgents/tradingagents', │ │
│ │ │ 'results_dir': './results', │ │
│ │ │ 'data_dir': '/Users/yluo/Documents/Code/ScAI/FR1-data', │ │
│ │ │ 'data_cache_dir': '/home/impen/workspace/playground/TradingAgents/tradingagents/dataflows/data_cach'+1, │ │
│ │ │ 'llm_provider': 'google', │ │
│ │ │ 'deep_think_llm': 'gemini-flash-latest', │ │
│ │ │ 'quick_think_llm': 'gemini-flash-latest', │ │
│ │ │ 'backend_url': 'https://generativelanguage.googleapis.com/v1', │ │
│ │ │ 'embedding_model': 'models/text-embedding-004', │ │
│ │ │ 'GOOGLE_API_KEY': 'AIzaSyBLKAflx8pDQMjO6omfc8XRQ25aXJcSOyw', │ │
│ │ │ ... +4 │ │
│ │ } │ │
│ │ selections = { │ │
│ │ │ 'ticker': 'SPY', │ │
│ │ │ 'analysis_date': '2025-11-14', │ │
│ │ │ 'analysts': [<AnalystType.MARKET: 'market'>], │ │
│ │ │ 'research_depth': 1, │ │
│ │ │ 'llm_provider': 'google', │ │
│ │ │ 'backend_url': 'https://generativelanguage.googleapis.com/v1', │ │
│ │ │ 'shallow_thinker': 'gemini-flash-latest', │ │
│ │ │ 'deep_thinker': 'gemini-flash-latest' │ │
│ │ } │ │
│ ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ │
│ /home/impen/workspace/playground/TradingAgents/tradingagents/graph/trading_graph.py:72 in **init** │
│ │
│ 69 │ │ self.toolkit = Toolkit(config=self.config) │
│ 70 │ │ │
│ 71 │ │ # Initialize memories │
│ ❱ 72 │ │ self.bull_memory = FinancialSituationMemory("bull_memory", self.config) │
│ 73 │ │ self.bear_memory = FinancialSituationMemory("bear_memory", self.config) │
│ 74 │ │ self.trader_memory = FinancialSituationMemory("trader_memory", self.config) │
│ 75 │ │ self.invest_judge_memory = FinancialSituationMemory( │
│ │
│ ╭──────────────────────────────────────────────────────────── locals ────────────────────────────────────────────────────────────╮ │
│ │ config = { │ │
│ │ │ 'project_dir': '/home/impen/workspace/playground/TradingAgents/tradingagents', │ │
│ │ │ 'results_dir': './results', │ │
│ │ │ 'data_dir': '/Users/yluo/Documents/Code/ScAI/FR1-data', │ │
│ │ │ 'data_cache_dir': │ │
│ │ '/home/impen/workspace/playground/TradingAgents/tradingagents/dataflows/data_cach'+1, │ │
│ │ │ 'llm_provider': 'google', │ │
│ │ │ 'deep_think_llm': 'gemini-flash-latest', │ │
│ │ │ 'quick_think_llm': 'gemini-flash-latest', │ │
│ │ │ 'backend_url': 'https://generativelanguage.googleapis.com/v1', │ │
│ │ │ 'embedding_model': 'models/text-embedding-004', │ │
│ │ │ 'GOOGLE_API_KEY': 'AIzaSyBLKAflx8pDQMjO6omfc8XRQ25aXJcSOyw', │ │
│ │ │ ... +4 │ │
│ │ } │ │
│ │ debug = True │ │
│ │ selected_analysts = ['market'] │ │
│ │ self = <tradingagents.graph.trading_graph.TradingAgentsGraph object at 0x72cc59439160> │ │
│ ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ │
│ /home/impen/workspace/playground/TradingAgents/tradingagents/agents/utils/memory.py:9 in **init** │
│ │
│ 6 class FinancialSituationMemory: │
│ 7 │ def **init**(self, name, config): │
│ 8 │ │ # Configure Gemini API │
│ ❱ 9 │ │ genai.configure(api_key=config.get("GOOGLE_API_KEY")) │
│ 10 │ │ │
│ 11 │ │ # Set embedding model based on config │
│ 12 │ │ if "embedding_model" in config: │
│ │
│ ╭─────────────────────────────────────────────────────── locals ───────────────────────────────────────────────────────╮ │
│ │ config = { │ │
│ │ │ 'project_dir': '/home/impen/workspace/playground/TradingAgents/tradingagents', │ │
│ │ │ 'results_dir': './results', │ │
│ │ │ 'data_dir': '/Users/yluo/Documents/Code/ScAI/FR1-data', │ │
│ │ │ 'data_cache_dir': '/home/impen/workspace/playground/TradingAgents/tradingagents/dataflows/data_cach'+1, │ │
│ │ │ 'llm_provider': 'google', │ │
│ │ │ 'deep_think_llm': 'gemini-flash-latest', │ │
│ │ │ 'quick_think_llm': 'gemini-flash-latest', │ │
│ │ │ 'backend_url': 'https://generativelanguage.googleapis.com/v1', │ │
│ │ │ 'embedding_model': 'models/text-embedding-004', │ │
│ │ │ 'GOOGLE_API_KEY': 'AIzaSyBLKAflx8pDQMjO6omfc8XRQ25aXJcSOyw', │ │
│ │ │ ... +4 │ │
│ │ } │ │
│ │ name = 'bull_memory' │ │
│ │ self = <tradingagents.agents.utils.memory.FinancialSituationMemory object at 0x72cc5943bcb0> │ │
│ ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
AttributeError: module 'google.genai' has no attribute 'configure'
