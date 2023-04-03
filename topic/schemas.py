import datetime
from pydantic import BaseModel
from typing import Optional


class TopicCreate(BaseModel):
    topic_name: str
    topic_answer: str = None
    url: str = None
    book_info: str = None
    video_link: str = None
    video_position: str = None
    related_topic: str = None
    created_date: datetime
    updated_date: datetime


class TopicView(BaseModel):
    tid: int
    topic_name: str
    topic_answer: str = None
    url: str = None
    book_info: str = None
    video_link: str = None
    video_position: str = None
    related_topic: str = None
    created_date: datetime
    updated_date: datetime
    is_active: bool


class TopicUpdate(BaseModel):
    topic_name: str
    topic_answer : str = None
    url: str = None
    book_info: str = None
    video_link: str = None
    video_position: str = None
    related_topic: str = None
    created_date: datetime
    updated_date: datetime
    is_active: bool

