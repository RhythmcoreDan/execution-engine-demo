# Execution Engine Demo

A minimal execution engine that turns trading signals into positions, realized PnL, and equity.  
This is a simplified, safe, public demo of how I structure an order/position layer inside a trading system.

---

## 🚀 What This Demo Shows

- Target position signals (`-1, 0, +1`)
- Position tracking (short, flat, long)
- Average entry price
- Realized PnL on closes and flips
- Unrealized PnL and running equity

Signals are interpreted as **target position**:
- `1`  → be long 1 unit  
- `0`  → be flat  
- `-1` → be short 1 unit  

Whenever the target changes, the engine:
1. Closes any existing position at the current price (realizing PnL)
2. Optionally opens a new position in the opposite direction
3. Tracks updated equity over time

---

## 📂 Project Structure

```text
execution-engine-demo/
│
├── execution_engine_demo.py   # Core execution engine
├── run_demo.py                # Demo runner
├── sample_signals.csv         # Example signal stream
└── README.md                  # Documentation
