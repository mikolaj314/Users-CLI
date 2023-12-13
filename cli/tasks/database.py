import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import create_engine


from cli.tasks.models import Base, Children, Users


class DatabaseManager:
    def __init__(self, database_url):
        self.database_url = database_url
        self.engine = create_engine(database_url)
        self.SessionLocal = so.sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        self.global_db = self.SessionLocal()

        Base.metadata.create_all(bind=self.engine)

    def populate_database_with(self, data):
        with self.SessionLocal() as session:
            for user_data in data:
                children_data = user_data.pop("children", [])
                user_db = Users(**user_data)

                for child_data in children_data:
                    child_db = Children(**child_data)
                    user_db.children.append(child_db)

                session.add(user_db)
            session.commit()

    def get_user_by_login(self, login, admin=False):
        columns = [Users.user_id, Users.email, Users.telephone_number, Users.password]

        if admin:
            columns.append(Users.role)

        statement = sa.select(*columns).where(
            sa.or_(Users.email == login, Users.telephone_number == login)
        )

        return self.global_db.execute(statement).first()

    def count_all_accounts(self):
        return self.global_db.query(Users).count()

    def get_oldest_account(self):
        return self.global_db.execute(
            sa.select(
                Users.firstname,
                Users.email,
                sa.func.min(Users.created_at).label("created_at"),
            )
        ).first()

    def get_age_grouped_by_children(self):
        return (
            self.global_db.query(Children.age, sa.func.count().label("count"))
            .group_by(Children.age)
            .order_by("count")
            .all()
        )

    def get_children(self, parent_id):
        return self.global_db.execute(
            sa.select(Children.name, Children.age)
            .select_from(Users)
            .join(Children, Children.user_id == Users.user_id)
            .where(Users.user_id == parent_id)
            .order_by(Children.name.asc())
        ).all()

    def get_children_with_user_children_same_age(self, parent_id):
        query = (
            sa.select(Users)
            .distinct()
            .join(Users.children)
            .options(so.selectinload(Users.children))
            .where(
                sa.and_(
                    Users.user_id != parent_id,
                    Children.age.in_(
                        sa.select(Children.age).where(Children.user_id == parent_id)
                    ),
                )
            )
        )
        return self.global_db.execute(query).all()
