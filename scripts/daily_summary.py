"""Daily sales summary for Frankie's Bite.
Usage: python daily_summary.py orders.csv order_items.csv 2026-11-04"""
import sys
import pandas as pd

orders, items, day = sys.argv[1], sys.argv[2], sys.argv[3]
o = pd.read_csv(orders)
i = pd.read_csv(items)
o["date"] = o["order_datetime"].str[:10]
d = o[o["date"] == day]
done = d[d["order_status"] != "cancelled"]
top_ch = done["channel"].value_counts().idxmax() if len(done) else "n/a"
top_item = (
    i[i["order_id"].isin(done["order_id"])]
    .groupby("product_name")["quantity"].sum().idxmax()
    if len(done) else "n/a"
)
print(f"Date: {day}")
print(f"Orders: {len(d)} | Cancelled: {(d['order_status']=='cancelled').sum()}")
print(f"Revenue (excl. cancelled): NGN {done['total_ngn'].sum():,.0f}")
print(f"Top channel: {top_ch}")
print(f"Top item: {top_item}")
