# Simple To-Do List API Security Check

## What’s This?
I’m a beginner learning Python and FastAPI by building a To-Do List API. I’ll check it for the OWASP API Security Top 10 (2023) vulnerabilities one by one to make it safer. Follow along or try it yourself!

## Project
A simple API to add, see, and delete to-do tasks.

## What You Need
- Python (any recent version)
- A code editor (like VS Code)

## Tools
- Python
- FastAPI (install with `pip install fastapi uvicorn`)

## To-Do List: Build and Check

### Step 1: Get Ready
- [ ] Install Python and check it works.
  - *Hint*: Type `python --version` in your terminal.
- [ ] Install FastAPI and Uvicorn.
  - *Hint*: Run `pip install fastapi uvicorn`.
- [ ] Make a folder (e.g., `todo-api`) and start a Git repo.
  - *Hint*: Use `git init`.

### Step 2: Build a Simple API
- [ ] Make a FastAPI app to show a task list.
  - *Hint*: Use `@app.get("/tasks")`.
- [ ] Add ways to add a task (`POST /tasks`) and delete a task (`DELETE /tasks/{id}`).
  - *Hint*: Store tasks in a list.
- [ ] Test it in your browser.
  - *Hint*: Run with `uvicorn` and go to `http://127.0.0.1:8000/tasks`.

### Step 3: Check #1 - Wrong Access (BOLA)
- [ ] See if you can delete someone else’s task.
  - *Hint*: Try `DELETE /tasks/1` with no check.
- [ ] Write in `notes.txt` if it’s a problem.
  - *Hint*: Should tasks belong to someone?

### Step 4: Check #2 - No Login (Broken Authentication)
- [ ] Test if anyone can use the API without logging in.
  - *Hint*: Just visit `/tasks`.
- [ ] Note in `notes.txt` if it’s too open.
  - *Hint*: Should it ask who you are?

### Step 5: Check #3 - Changing Too Much (Broken Property Authorization)
- [ ] Try changing a task with weird data.
  - *Hint*: Send a `POST /tasks` with extra stuff.
- [ ] Write in `notes.txt` what happens.
  - *Hint*: Does it stop bad changes?

### Step 6: Check #4 - Too Much Stuff (Resource Consumption)
- [ ] Add a giant task and see if it breaks.
  - *Hint*: Make a super long task name.
- [ ] Note in `notes.txt` if it’s slow or crashes.
  - *Hint*: Should it limit big inputs?

### Step 7: Check #5 - Wrong Permissions (Function Authorization)
- [ ] Test if everyone can do everything.
  - *Hint*: Add a special action and try it.
- [ ] Write in `notes.txt` if it’s wrong.
  - *Hint*: Should some things be locked?

### Step 8: Check #6 - Overusing It (Sensitive Flows)
- [ ] Try deleting tasks a lot.
  - *Hint*: Keep hitting `DELETE /tasks/{id}`.
- [ ] Note in `notes.txt` if it’s bad.
  - *Hint*: Should it stop you after a bit?

### Step 9: Check #7 - Tricking the Server (SSRF)
- [ ] Add a way to fetch a link, test a weird one.
  - *Hint*: Make a `/fetch` and try a local address.
- [ ] Write in `notes.txt` if it’s risky.
  - *Hint*: Should it block strange links?

### Step 10: Check #8 - Bad Setup (Security Misconfiguration)
- [ ] Look for mistakes like showing errors.
  - *Hint*: Cause an error and see what shows.
- [ ] Note in `notes.txt` what’s wrong.
  - *Hint*: Should errors be secret?

### Step 11: Check #9 - Old Stuff (Inventory Management)
- [ ] Add then remove a feature, see if it stays.
  - *Hint*: Test an old `/test` link.
- [ ] Write in `notes.txt` if it’s still there.
  - *Hint*: Should old things go away?

### Step 12: Check #10 - Trusting Bad Data (Unsafe APIs)
- [ ] Pretend to use another API, send junk.
  - *Hint*: Make a fake call with bad info.
- [ ] Note in `notes.txt` if it breaks.
  - *Hint*: Should it check the data?

### Step 13: Fix and Share
- [ ] Fix one problem (like #1).
  - *Hint*: Add a simple check, like “is this your task?”
- [ ] Test it and write how it went in `notes.txt`.
  - *Hint*: Did it work better?
- [ ] Put your code on GitHub.
  - *Hint*: Use `git add`, `git commit`, `git push`.

## Help Out
Try it yourself or tell me ideas in GitHub!

## Where to Learn More
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [FastAPI Website](https://fastapi.tiangolo.com/)
