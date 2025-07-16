from app.parser.codeforces_parser import fetch_problems

def test_fetch_problems():
    problems, stats = fetch_problems()
    assert isinstance(problems, list)
    assert isinstance(stats, dict)
