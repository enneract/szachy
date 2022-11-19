from szachy.web import _abbreviate_name, _format_score


def test_abbreviate_name() -> None:
    assert _abbreviate_name('Smith') == 'Smith'
    assert _abbreviate_name('John Smith') == 'J. Smith'
    assert _abbreviate_name('John James Smith') == 'J. J. Smith'


def test_format_score() -> None:
    assert _format_score(0) == '0'
    assert _format_score(1) == '0.5'
    assert _format_score(2) == '1'
    assert _format_score(3) == '1.5'
    assert _format_score(4) == '2'
    assert _format_score(5) == '2.5'
    assert _format_score(6) == '3'
    assert _format_score(1237940039285380274899124224) == '618970019642690137449562112'
    assert _format_score(1237940039285380274899124225) == '618970019642690137449562112.5'
