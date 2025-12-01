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

🧪 How to Run

Install dependencies:

pip install pandas

Run the demo:

python run_demo.py

📊 Example Output

=== EXECUTION ENGINE DEMO ===
2024-01-01 | price=1.10000 | signal=0 | pos=0 | avg=0.00000 | realized=0.00000 | equity=0.00000
2024-01-02 | price=1.10200 | signal=1 | pos=1 | avg=1.10200 | realized=0.00000 | equity=0.00000
2024-01-03 | price=1.10450 | signal=1 | pos=1 | avg=1.10200 | realized=0.00000 | equity=0.00250
2024-01-04 | price=1.10600 | signal=1 | pos=1 | avg=1.10200 | realized=0.00000 | equity=0.00400
2024-01-05 | price=1.10750 | signal=0 | pos=0 | avg=0.00000 | realized=0.00550 | equity=0.00550
...
Final state:
position=0, realized_pnl=0.0XXXXX, equity=0.0XXXXX

🧠 About This Project

This repo demonstrates how I think about the "hands" of a trading system:

turning abstract signals into concrete positions

tracking entries, exits, and running PnL

keeping the logic simple, explicit, and testable

In my full system (RhythmCore), this type of execution layer is wired to:

emotional/behavior engines

regime detection

live data feeds

alerting/monitoring channels

risk controls and sizing

If you'd like to integrate an execution engine into your own strategy or bot, I'm open to collaboration.


---

Once you’ve got those three files + the README in place, repo 4 is done and your GitHub basically says:

> “I build **full trading systems front-to-back**.”

When you’re finished, you can just tell me something like:

> “Execution repo is in.”

And then, if you want, we can:

- Pin this repo along with the others  
- Write a one-liner that ties all 4 modules together for your profile  
- Start using these links in messages to clients / posts you reply to
::contentReference[oaicite:0]{index=0}

