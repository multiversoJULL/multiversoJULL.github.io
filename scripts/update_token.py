import json, urllib.request, datetime, os

URL = "https://wowtokenprice.com/api/v1/tokens/prices"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "token.json")

req = urllib.request.Request(URL, headers={"User-Agent": "jullverse-site/1.0"})
raw = json.load(urllib.request.urlopen(req, timeout=40))

res = {}
for it in raw.get("data", []):
    if it.get("gameVersion") != "retail":
        continue
    reg = it.get("region")
    if reg in ("eu", "us") and it.get("priceGold"):
        res[reg] = {
            "price": int(it["priceGold"]),
            "at": it.get("sourceUpdatedAt") or it.get("fetchedAt"),
        }

if "eu" not in res or "us" not in res:
    raise SystemExit("la API no devolvio ambas regiones")

res["updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
old = None
if os.path.exists(OUT):
    try:
        old = json.load(open(OUT, encoding="utf-8"))
    except Exception:
        old = None

if old and old.get("eu", {}).get("price") == res["eu"]["price"] and \
   old.get("us", {}).get("price") == res["us"]["price"]:
    print("sin cambios")
else:
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("actualizado:", res["eu"]["price"], res["us"]["price"])
