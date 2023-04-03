from utils.dbUtil import database
from topic import schemas as topic_schema


def create_topic(topic: topic_schema.TopicCreate):
    query = "INSERT INTO topic (nextval('topic_id_seq'), " \
            ":topic_name, :topic_answer ,:url, " \
            ":book_info, :video_link , :video_position, :related_topic, now() at time zone 'UTC' ," \
            "now() at time zone 'UTC' , :is_active ) RETURNING topic.vid"

    return database.execute(query, values={"topic_name": topic.vendor_name,
                                           "topic_answer": topic.topic_answer,
                                           "url": topic.url,
                                           "book_info": topic.book_info,
                                           "video_link": topic.video_link,
                                           "video_position": topic.video_position,
                                           "related_topic": topic.related_topic,
                                           "is_active":True
                                           })


def update_topic(topic_id, topic_update: topic_schema.TopicUpdate):
    query = "update topic set topic_name=:topic_name, " \
            "topic_answer=:topic_answer ,url=:url, " \
            "book_info=:book_info, video_link=:video_link ," \
            "video_position=:video_position, related_topic=:related_topic," \
            "updated_date=now() at time zone 'UTC' ," \
            " is_active=:is_active where tid=:topic_id"
    return database.execute(query, values={"topic_name": topic_update.topic_name,
                                           "topic_answer": topic_update.topic_answer,
                                           "url": topic_update.url,
                                           "book_info": topic_update.book_info,
                                           "video_link": topic_update.video_link,
                                           "video_position": topic_update.video_position,
                                           "related_topic": topic_update.related_topic,
                                           "is_active": topic_update.is_active,
                                           "topic_id":topic_id
                                           })


def delete_topic_by_id(topic_id):
    query = "delete from topic where tid=:topic_id"
    return database.execute(query, values={"topic_id": topic_id})


def get_topic_by_id(topic_id):
    query = "select * from topic where tid=:topic_id"
    return database.execute(query, values={"topic_id": topic_id})






