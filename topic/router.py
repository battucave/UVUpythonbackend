import shutil
from typing import List
import random

from fastapi import APIRouter, HTTPException, File, Depends, UploadFile
from topic import schemas as topic_schema
from topic import curd
import os
import Exception
from exceptions.business import BusinessException

from fastapi.responses import FileResponse



router = APIRouter(
    prefix='/api/v1'
)


@router.post("/topic", response_model=topic_schema.TopicView)
async def create_topic( topic: topic_schema.TopicCreate= Depends()):
    try:
        tid = await curd.create_topic(topic)
        return await curd.get_topic_by_id(tid)
    except Exception as e:
        return {"detail": "Failed to create topic"}


@router.put("/topic/{topic_id}", response_model=topic_schema.TopicView)
async def update_vendor(topic_id: int, update: topic_schema.TopicUpdate = Depends()):
    try:
        tid = await curd.update_topic(update)
        return await curd.get_topic_by_id(tid)
    except Exception as e:
        return {"detail": "Failed to update topic"}


@router.delete("/topic/{topic_id}")
async def update_vendor(topic_id: int):
    try:
        tid = await curd.delete_topic_by_id(topic_id)
        return {"code": 200, "detail": "Topic deleted"}
    except Exception as e:
        return {"detail": "Failed to delete topic"}


@router.get("/topic/{topic_id}", response_model=topic_schema.TopicView)
async def update_vendor(topic_id: int):
    try:
        tid = await curd.get_topic_by_id(topic_id)
    except Exception as e:
        return {"detail": "Failed to get topic details"}