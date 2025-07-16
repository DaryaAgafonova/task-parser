import requests
from app.database import SessionLocal
from app.models import Problem, Tag

def fetch_problems():
    url = "https://codeforces.com/api/problemset.problems"
    resp = requests.get(url)
    data = resp.json()["result"]
    problems = data["problems"]
    stats = {f"{p['contestId']}{p['index']}": p for p in data["problemStatistics"]}
    return problems, stats

def update_problems():
    session = SessionLocal()
    problems, stats = fetch_problems()
    for p in problems:
        key = f"{p['contestId']}{p['index']}"
        solved = stats.get(key, {}).get("solvedCount", 0)
        db_problem = session.query(Problem).filter_by(contest_id=p["contestId"], index=p["index"]).first()
        if not db_problem:
            db_problem = Problem(
                contest_id=p["contestId"],
                index=p["index"],
                name=p["name"],
                rating=p.get("rating"),
                solved_count=solved
            )
            session.add(db_problem)
        else:
            db_problem.rating = p.get("rating")
            db_problem.solved_count = solved
        for tag_name in p.get("tags", []):
            tag = session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                session.add(tag)
            if tag not in db_problem.tags:
                db_problem.tags.append(tag)
    session.commit()
    session.close()
