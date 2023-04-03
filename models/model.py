from sqlalchemy import Table, \
    Column, Integer, String, DateTime, \
    MetaData, Sequence,  \
    Boolean, Numeric , TEXT
import datetime

metadata = MetaData()

topic = Table(
    'topic', metadata,
    Column('tid', Integer, Sequence('topic_id_seq'), primary_key=True),
    Column('topic_name', String(5000), nullable=False),
    Column('topic_answer', String(10000), nullable=True),
    Column('url', String(10000), nullable=True),
    Column('book_info', String(5000), nullable=True),
    Column('video_link', String(5000), nullable=True),
    Column('video_position', String(5000), nullable=True),
    Column('related_topic', String(5000), nullable=True),
    Column('created_date', DateTime, default=datetime.datetime.utcnow, nullable=False),
    Column('updated_date', DateTime, default=datetime.datetime.utcnow, nullable=False),
    Column('is_active', Boolean, default=True)
)
