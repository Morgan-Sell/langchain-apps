from typing import Dict, List, Any

from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.outputs import LLMResult


class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        **kwargs: Any,
    ) -> Any:
        """Run when LLM starts running"""
        print(f"***Prompt to LLM was: ***\n{prompts[0]}")
        print("********")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM provides a response"""
        print(f"***LLM Response:***\n{response.generations[0][0].text}")
        print("**********")
