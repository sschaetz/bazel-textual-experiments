
import sys
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from python.runfiles import runfiles
from pathlib import Path

def _get_runfile(name: str) -> Path:
    r = runfiles.Create()
    return Path(r.Rlocation(name))

class InterpreterInfo(Static):
    def on_mount(self) -> None:
        interpreter_path = sys.executable
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        self.update(f"Python Interpreter: {interpreter_path}\nPython Version: {python_version}")

class ExampleApp(App):
    """A Textual example app."""
    
    CSS_PATH = _get_runfile("_main/src/example.tcss") 
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield InterpreterInfo()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = ExampleApp()
    app.run()
