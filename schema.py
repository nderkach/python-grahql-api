from graphene import ObjectType, String, Boolean, ID, List, Field, Int
from airbnb import Api
import json
import os
from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


class User(ObjectType):
    first_name = String()
    has_profile_pic = Boolean()
    id = ID()
    picture_url = String()
    smart_name = String()
    thumbnail_url = String()


class Listing(ObjectType):
    id = ID()
    name = String()


class Review(ObjectType):
    author = Field(User)
    author_id = ID()
    can_be_edited = Boolean()
    comments = String()
    created_at = String()
    id = Int()
    language = String()
    listing = Field(Listing)
    listing_id = ID()
    recipient = Field(User)
    recipient_id = ID()
    response = String()
    role = String()
    user_flag = Boolean()


class Query(ObjectType):
    reviews = List(Review, id=Int(required=True))

    def resolve_reviews(self, args, context, info):
        api = Api(os.environ.get("AIRBNB_LOGIN"),
                  os.environ.get("AIRBNB_PASSWORD"))
        return json2obj(json.dumps(api.get_reviews(args.get("id"))["reviews"]))