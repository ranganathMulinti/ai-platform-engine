from core.database.session import get_db
from sqlalchemy.orm import Session


def test_get_db_dependency() -> None:
    """Test that get_db yields a SQLAlchemy session."""

    generator = get_db()

    db = next(generator)

    try:
        assert isinstance(db, Session)
    finally:
        generator.close()
