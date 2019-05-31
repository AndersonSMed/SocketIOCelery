import mongoengine
import datetime


class Channel(mongoengine.EmbeddedDocument):
    _id = mongoengine.IntField()
    description = mongoengine.StringField()
    private_video = mongoengine.BooleanField()
    broadcaster_software = mongoengine.StringField()
    broadcaster_language = mongoengine.StringField()
    privacy_options_enabled = mongoengine.BooleanField()
    broadcaster_type = mongoengine.StringField()
    display_name = mongoengine.StringField()
    followers = mongoengine.IntField()
    game = mongoengine.StringField()
    language = mongoengine.StringField()
    logo = mongoengine.StringField()
    mature = mongoengine.BooleanField()
    name = mongoengine.StringField()
    partner = mongoengine.BooleanField()
    profile_banner = mongoengine.StringField()
    profile_banner_background_color = mongoengine.StringField()
    status = mongoengine.StringField()
    url = mongoengine.StringField()
    video_banner = mongoengine.StringField()
    views = mongoengine.IntField()

class Preview(mongoengine.EmbeddedDocument):
    large = mongoengine.StringField()
    medium = mongoengine.StringField()
    small = mongoengine.StringField()
    template = mongoengine.StringField()

class Stream(mongoengine.Document):
    _id = mongoengine.IntField()
    broadcast_platform = mongoengine.StringField()
    community_id = mongoengine.StringField()
    community_ids = mongoengine.ListField()
    video_height = mongoengine.IntField()
    average_fps = mongoengine.IntField()
    is_playlist = mongoengine.BooleanField()
    stream_type = mongoengine.StringField()
    date_fetch = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    channel = mongoengine.EmbeddedDocumentField(Channel)
    delay = mongoengine.IntField()
    game = mongoengine.StringField()
    preview = mongoengine.EmbeddedDocumentField(Preview)
    viewers = mongoengine.IntField()