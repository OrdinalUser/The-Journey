import plotly.graph_objects as go
from plotly.subplots import make_subplots

def collatz_sequence(n: int) -> list[int]:
    """Generate the full Collatz sequence starting from n."""
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def plot_collatz(start: int, end: int) -> None:
    """Plot Collatz trajectories for all integers in [start, end]."""
    fig = go.Figure()

    for n in range(start, end + 1):
        seq = collatz_sequence(n)
        fig.add_trace(go.Scatter(
            y=seq,
            mode='lines',
            line=dict(width=0.6),
            opacity=0.5,
            name=f'n={n}',
            showlegend=False  # Hide individual traces from legend to avoid clutter
        ))

    fig.update_layout(
        title=f"Collatz trajectories for n = {start}..{end}",
        xaxis_title="Step",
        yaxis_title="Value",
        yaxis_type="log",  # Equivalent to set_yscale("log")
        width=1200,
        height=600,
        template="plotly_white"  # Clean, modern look
    )

    fig.show()

if __name__ == "__main__":
    plot_collatz(1, 200)