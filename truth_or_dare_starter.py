"""
Starter template: Truth or Dare (Python)

Complete the TODO sections to build your own working game.
"""

from __future__ import annotations

import random


class TruthOrDareGame:
    def __init__(self) -> None:
        # TODO: Replace starter values with your own setup logic.
        self.players: list[str] = []
        self.truth_prompts: list[str] = []
        self.dare_prompts: list[str] = []

    def setup_players(self) -> None:
        """TODO: Ask for player names and store them in self.players."""
        raise NotImplementedError("Implement setup_players()")

    def load_prompts(self) -> None:
        """TODO: Add truth and dare prompts to the lists."""
        raise NotImplementedError("Implement load_prompts()")

    def choose_player(self) -> str:
        """TODO: Return a random player from self.players."""
        raise NotImplementedError("Implement choose_player()")

    def choose_prompt(self, challenge_type: str) -> str:
        """TODO: Return a random truth/dare prompt based on challenge_type."""
        raise NotImplementedError("Implement choose_prompt()")

    def play_round(self) -> None:
        """TODO: Run one round of Truth or Dare."""
        raise NotImplementedError("Implement play_round()")

    def run(self) -> None:
        """TODO: Run setup and loop through rounds until players quit."""
        raise NotImplementedError("Implement run()")


def print_project_tips() -> None:
    """Print beginner-friendly requirements and tips."""
    print("Project requirements:")
    print("1) Collect player names")
    print("2) Add truth and dare prompts")
    print("3) Randomly pick a player")
    print("4) Let them choose truth or dare")
    print("5) Show a random matching prompt")
    print("6) Repeat until users quit")
    print()
    print("Tips:")
    print("- Implement one method at a time")
    print("- Test each method before moving on")
    print("- Handle empty lists and invalid inputs")


if __name__ == "__main__":
    print("Truth or Dare - Starter Template")
    print_project_tips()
    game = TruthOrDareGame()
    # TODO: Uncomment after implementing methods:
    # game.run()
