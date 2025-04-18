# ui_poc/agent_interface.py
class AgentInterface:
    def process_input(self, user_input: str) -> str:
        return f"[Mock Reply] You said: {user_input}"
