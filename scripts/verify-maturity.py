#!/usr/bin/env python3
"""Verify every package in pnpm-lock.yaml was published >= 12 days (288 h) ago.
Stdlib only. Missing timestamps fail. Exit 1 on any failure."""
import json, re, sys, urllib.request, datetime, concurrent.futures, pathlib
lock = pathlib.Path(__file__).resolve().parent.parent / "pnpm-lock.yaml"
text = lock.read_text()
section = text.split("\npackages:\n", 1)[1].split("\nsnapshots:\n", 1)[0]
keys = re.findall(r"^  '?(@?[^@\s'][^@\s']*)@([^:'(\s]+)'?:", section, re.M)
now = datetime.datetime.now(datetime.timezone.utc)
def check(item):
    name, ver = item
    url = "https://registry.npmjs.org/" + name.replace("/", "%2F")
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    data = json.load(urllib.request.urlopen(req, timeout=60))
    t = data.get("time", {}).get(ver)
    if not t: return name, ver, None, "MISSING TIME"
    age = (now - datetime.datetime.fromisoformat(t.replace("Z", "+00:00"))).total_seconds() / 3600
    return name, ver, t, "ok" if age >= 288 else f"TOO NEW ({age:.0f} h)"
with concurrent.futures.ThreadPoolExecutor(12) as ex:
    rows = sorted(ex.map(check, keys))
bad = [r for r in rows if r[3] != "ok"]
youngest = max((r for r in rows if r[2]), key=lambda r: r[2])
print(f"checked {len(rows)} exact versions; failures {len(bad)}; youngest {youngest[0]}@{youngest[1]} {youngest[2]}")
for r in bad: print("FAIL", *r)
sys.exit(1 if bad else 0)
