import typer

from src.simulation import run_simulation

app = typer.Typer()


@app.command()
def run(
    steps: int = typer.Option(200, min=1, help="Количество шагов симуляции, > 0"),
    seed: int | None = typer.Option(16, help="Сид для генератора случайных чисел"),
):
    run_simulation(steps, seed)


if __name__ == "__main__":
    app()
