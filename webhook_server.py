from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/github")
async def github_webhook(request: Request):
    payload = await request.json()

    print("\n===== GitHub Webhook =====")
    print("Event      :", request.headers.get("X-GitHub-Event"))
    print("Repository :", payload["repository"]["full_name"])
    print("Branch     :", payload["ref"])
    print("Pusher     :", payload["pusher"]["name"])

    return {"status": "received"}