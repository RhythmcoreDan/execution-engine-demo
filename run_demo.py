"""
run_demo.py
-----------
Runs the demo execution engine on a small set of signals
and prints position + PnL over time.
"""

import pandas as pd
from execution_engine_demo import run_execution


def main():
    df = pd.read_csv("sample_signals.csv")

    result = run_execution(df)

    print("=== EXECUTION ENGINE DEMO ===")
    for _, row in result.iterrows():
        print(
            f"{row['time']} | price={row['price']:.5f} | "
            f"signal={int(row['signal'])} | pos={int(row['position'])} | "
            f"avg={row['avg_price']:.5f} | "
            f"realized={row['realized_pnl']:.5f} | equity={row['equity']:.5f}"
        )

    last = result.iloc[-1]
    print("\nFinal state:")
    print(
        f"position={int(last['position'])}, "
        f"realized_pnl={last['realized_pnl']:.5f}, "
        f"equity={last['equity']:.5f}"
    )


if __name__ == "__main__":
    main()
