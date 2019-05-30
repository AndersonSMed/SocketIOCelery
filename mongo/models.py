from mongoengine import *
import datetime


class Channel(EmbeddedDocument):
    id = IntField()
    broadcaster_language = StringField()
    created_at = DateTimeField()
    display_name = StringField()
    followers = IntField()
    game = StringField()
    language = StringField()
    logo = StringField()
    mature = BooleanField()
    name = StringField()
    partner = BooleanField()
    profile_banner = StringField()
    profile_banner_background_color = StringField()
    status = StringField()
    updated_at = DateTimeField()
    url = StringField()
    video_banner = StringField()
    views = IntField()

class Preview(EmbeddedDocument):
    large = StringField()
    medium = StringField()
    small = StringField()
    template = StringField()

class Stream(EmbeddedDocument):
    id = StringField()
    date_fetch = DateTimeField(default=datetime.datetime.utcnow)
    channel = EmbeddedDocumentField(Channel)
    created_at = DateTimeField()
    delay = IntField()
    game = StringField()
    preview = {}
    viewers = IntField()