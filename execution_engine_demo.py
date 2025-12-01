"""
execution_engine_demo.py
------------------------
Minimal execution engine that turns target position signals into:
- position
- realized PnL
- running equity

This is a simplified, safe, public demo of how an order/position engine can work.
"""

from __future__ import annotations

import pandas as pd


def run_execution(signals_df: pd.DataFrame) -> pd.DataFrame:
    """
    signals_df must contain:
      - time
      - price
      - signal  (target position: -1, 0, +1)

    We assume:
      - position size is either -1, 0, or +1 unit
      - fills occur at the given price
      - no fees/slippage (for demo simplicity)
    """
    position = 0        # -1 (short), 0 (flat), +1 (long)
    avg_price = 0.0
    realized_pnl = 0.0

    rows = []

    for _, row in signals_df.iterrows():
        time = row["time"]
        price = float(row["price"])
        target = int(row["signal"])

        # Change in position
        if target != position:
            # Closing existing position if needed
            if position == 1 and target <= 0:
                # closing long
                realized_pnl += (price - avg_price) * 1.0
                position = 0
                avg_price = 0.0

            elif position == -1 and target >= 0:
                # closing short
                realized_pnl += (avg_price - price) * 1.0
                position = 0
                avg_price = 0.0

            # Crossing directly from long to short or short to long
            if position == 0 and target != 0:
                # open new position at current price
                position = target
                avg_price = price

        # Unrealized PnL
        if position == 1:
            unrealized = (price - avg_price) * 1.0
        elif position == -1:
            unrealized = (avg_price - price) * 1.0
        else:
            unrealized = 0.0

        equity = realized_pnl + unrealized

        rows.append(
            {
                "time": time,
                "price": price,
                "signal": target,
                "position": position,
                "avg_price": avg_price,
                "realized_pnl": round(realized_pnl, 5),
                "equity": round(equity, 5),
            }
        )

    return pd.DataFrame(rows)
