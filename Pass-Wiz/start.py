from time import sleep
from rich.console import Console

console = Console()
tasks = [f"[bold cyan]Successfully launched! " for n in range(1, 2)]

with console.status("[bold cyan]Launch Pass-Wiz please wait a few seconds ...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(5)
        console.log(f"{task} Pass-Wiz")
