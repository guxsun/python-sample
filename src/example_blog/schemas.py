from datetime import datetime
"""
类型注解
"""
from typing import Optional, TypeVar
"""
数据验证
"""
from pydantic import BaseModel, constr

from example_blog.models import BaseModel as DBModel
"""
ModelType：这个类型变量类似于 Java 泛型中的 <T>，它表示可以接受任何类型，
但必须是 DBModel 或其子类的类型。在 Java 中，
你可能会看到类似 <T extends DBModel> 的泛型定义，其中 T 必须是 DBModel 或其子类
"""
ModelType = TypeVar('ModelType', bound=DBModel)
"""
这两个类型变量分别表示用于创建和更新的数据模型或 DTO（数据传输对象）。
它们也类似于 Java 泛型中的 <T>，但必须是 BaseModel 或其子类的类型
"""
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)


class InDBMixin(BaseModel):
    id: int

    class Config:
        orm_mode = True


class BaseArticle(BaseModel):
    title: constr(max_length=500)
    body: Optional[str] = None


class ArticleSchema(BaseArticle, InDBMixin):
    create_time: datetime
    update_time: datetime


class CreateArticleSchema(BaseArticle):
    pass


class UpdateArticleSchema(BaseArticle):
    title: Optional[constr(max_length=500)] = None