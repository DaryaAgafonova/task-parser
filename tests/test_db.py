from app.models import Problem, Tag

def test_problem_model():
    p = Problem(contest_id=1, index='A', name='Test', rating=800, solved_count=10)
    assert p.name == 'Test'
    assert p.rating == 800

def test_tag_model():
    t = Tag(name='math')
    assert t.name == 'math'
