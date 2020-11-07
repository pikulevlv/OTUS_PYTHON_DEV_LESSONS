from sqlalchemy.ext.declarative import declarative_base # model's basis
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import sessionmaker, scoped_session, relationship


engine = create_engine("sqlite:///example2.db") # can create the file anywhere
Base = declarative_base(bind=engine) # bind helps metadata to use engine

# make a session factory and bind with the engine
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# промежуточная таблица между постами и тегами
posts_tags_table = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow) # can give a function (not instance) in default, not only var
    #make a table
    posts: list = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})" # representation !r
    def __repr__(self):
        return str(self)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False) # if we wright below class User
    # author_id = Column(Integer, ForeignKey("users.id"), nullable=False) # if we wright above class User. "users" - table's name
    # ForeignKey - one to many relation
    author = relationship(User, back_populates="posts")
    # author = relationship("User", back_populates="posts) # equal
    tags = relationship("Tag", secondary=posts_tags_table, back_populates="posts") #secondary - вторичная (промежуточная) таблица

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})"

    def __repr__(self):
        return str(self)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    posts = relationship("Post", secondary=posts_tags_table, back_populates="tags")


    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"
    def __repr__(self):
        return str(self)

def create_user(username: str) -> User:
    u = User(username="sam")
    print("id before", u.id)
    session.add(u) # add user
    session.commit() # commit in DB
    print("id after", u.id)
    return u

def author_posts():
    user: User = session.query(User).filter_by(username = "sam").one()
    print(user)
    post = Post(title="First post!")
    session.add(post)
    session.commit()
    print(post)
    print(user.posts)

    post = Post(title="Second post!")
    # session.add(post)
    # session.commit()
    user.posts.append(post)
    # user_posts: List[Post] = user.posts
    session.commit()
    print(user.posts)

def create_tags():
    user = session.query(User).filter_by(username = "john").one()
    user.is_staff = True
    tags = [Tag(name=n) for n in ("news", "flask", "django", "python")]
    post = Post(title="News Flask vs django", author=user)
    # Дополняет массив элементами из объекта, поддерживающего итерирование
    post.tags.extend(tags)
    session.commit()

    print(post, post.tags)
    for tag in tags:
        print(tag, tag.posts)

if __name__ == '__main__':
    Base.metadata.create_all()
    session = Session() # instance class
    # u = create_user("sam")
    # author_posts()
    # create_tags()
    users = session.query(User).filter(
        User.id > 1,
        User.username != "john",
    ).all()

    print(users)

    posts = session.query(Post).all()
    for post in posts:
        print(post, type(post.tags))

    # for tag in tags:
    #     print(tag, tag.posts)
    users_query = session.query(
        User,
    ).join(
        Post,
        User.id == Post.author_id,
    ).filter(
        Post.tags.any(
            # Tag.name.ilike("new%"),
            Tag.name != "django",
                      )
    ).all()

    print(users_query)
    # print(users_query.all())

    posts_query = session.query(
        Post,
    ).filter(
        Post.tags.any(
            # Tag.name.ilike("new%"),
            # Tag.name != "django",
            Tag.name == "flask",
                      )
    )
    print(posts_query) # это объект запроса (до выполнения самого запроса)
    print(repr(posts_query))
    print(posts_query.all())
    session.close() # need to close session


# 57:49 many-to-many
