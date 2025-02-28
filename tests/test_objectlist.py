import pytest

import pikepdf


@pytest.fixture
def pal(resources):
    with pikepdf.open(resources / 'pal.pdf') as pdf:
        yield pdf


def test_objectlist_repr(pal):
    cs = pikepdf.parse_content_stream(pal.pages[0].Contents)
    assert isinstance(cs[1][0], pikepdf._qpdf._ObjectList)
    ol = cs[1][0]
    assert (
        "[Decimal('144.0000'), 0, 0, Decimal('144.0000'), Decimal('0.0000'), Decimal('0.0000')]"
        in repr(ol)
    )
