import json
import time

from tradingagents.agents.utils.agent_utils import extract_content_string


def create_risk_manager(llm, memory):
    def risk_manager_node(state) -> dict:
        company_name = state["company_of_interest"]

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        market_research_report = extract_content_string(state["market_report"])
        news_report = extract_content_string(state["news_report"])
        fundamentals_report = extract_content_string(state["news_report"])
        sentiment_report = extract_content_string(state["sentiment_report"])
        trader_plan = state["investment_plan"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1):
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""As the Risk Management Judge and Debate Facilitator, your goal is to evaluate the debate between three risk analysts—Risky, Neutral, and Safe/Conservative—and determine the best course of action for the trader. Your decision must result in a clear recommendation: Buy, Sell, or Hold, accompanied by a specific **Time Frame**. Choose Hold only if strongly justified by specific arguments. Strive for clarity and decisiveness.

Guidelines for Decision-Making:
1. **Summarize Key Arguments**: Extract the strongest points from each analyst, focusing on relevance to the context.
2. **Define the Time Frame**: Based on the volatility and the arguments presented, explicitly specify the suitable time horizon for this trade (e.g., Scalping [minutes], Intraday [hours], Swing [days], or Long-term).
3. **Provide Rationale**: Support your recommendation with direct quotes and counterarguments from the debate.
4. **Refine the Trader's Plan**: Start with the trader's original plan, **{trader_plan}**, and adjust it based on the analysts' insights.
5. **Learn from Past Mistakes**: Use lessons from **{past_memory_str}** to address prior misjudgments and ensure you don't repeat a wrong BUY/SELL/HOLD call.

Deliverables:
- **Final Decision**: Buy, Sell, or Hold.
- **Time Frame**: Specific duration validity (e.g., "Intraday: 4-8 hours" or "Scalping: Exit within 30 mins").
- **Detailed Reasoning**: Anchored in the debate and past reflections.

---

**Analysts Debate History:**  
{history}

---

Focus on actionable insights. Build on past lessons, critically evaluate all perspectives, and ensure the decision includes *when* to act and *how long* to hold.
**ตอบทั้งหมดนี้เป็นภาษาไทย โดยใช้คำศัพท์เทรดที่เหมาะสม ดูเป็นมืออาชีพ และเป็นธรรมชาติ (เช่น ใช้คำว่า 'กรอบเวลา', 'ระยะสั้น', 'รันเทรนด์')**
"""

        response = llm.invoke(prompt)

        new_risk_debate_state = {
            "judge_decision": response.content,
            "history": risk_debate_state["history"],
            "risky_history": risk_debate_state["risky_history"],
            "safe_history": risk_debate_state["safe_history"],
            "neutral_history": risk_debate_state["neutral_history"],
            "latest_speaker": "Judge",
            "current_risky_response": risk_debate_state["current_risky_response"],
            "current_safe_response": risk_debate_state["current_safe_response"],
            "current_neutral_response": risk_debate_state["current_neutral_response"],
            "count": risk_debate_state["count"],
        }

        return {
            "risk_debate_state": new_risk_debate_state,
            "final_trade_decision": response.content,
        }

    return risk_manager_node
