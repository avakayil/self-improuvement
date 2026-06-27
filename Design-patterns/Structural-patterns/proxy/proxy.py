from abc import ABC, abstractmethod
import time


# =====================================
# Subject
# =====================================

class ThirdPartyYoutubeLib(ABC):

    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, video_id):
        pass

    @abstractmethod
    def download_video(self, video_id):
        pass


# =====================================
# Real Subject
# =====================================

class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):

    def list_videos(self):
        print("Fetching video list from YouTube...")
        time.sleep(2)
        return ["Python", "Design Patterns", "System Design"]

    def get_video_info(self, video_id):
        print(f"Fetching info for {video_id}...")
        time.sleep(2)
        return f"Information about {video_id}"

    def download_video(self, video_id):
        print(f"Downloading {video_id}...")
        time.sleep(2)
        print("Download Complete")


# =====================================
# Proxy
# =====================================

class CachedYoutubeClass(ThirdPartyYoutubeLib):

    def __init__(self, service):
        self.service = service

        self.list_cache = None
        self.video_cache = {}

        self.need_reset = False

    def list_videos(self):

        if self.list_cache is None or self.need_reset:

            print("Cache Miss")

            self.list_cache = self.service.list_videos()

        else:
            print("Cache Hit")

        return self.list_cache

    def get_video_info(self, video_id):

        if (
            video_id not in self.video_cache
            or self.need_reset
        ):

            print("Cache Miss")

            self.video_cache[video_id] = \
                self.service.get_video_info(video_id)

        else:
            print("Cache Hit")

        return self.video_cache[video_id]

    def download_video(self, video_id):
        self.service.download_video(video_id)


# =====================================
# Client
# =====================================

class YoutubeManager:

    def __init__(self, service):
        self.service = service

    def render_video_page(self, video_id):

        info = self.service.get_video_info(video_id)

        print(info)

    def render_list_panel(self):

        videos = self.service.list_videos()

        print(videos)

    def react_on_user_input(self):

        self.render_list_panel()

        self.render_video_page("abc123")

        print()

        self.render_list_panel()

        self.render_video_page("abc123")


# =====================================
# Main
# =====================================

youtube_service = ThirdPartyYoutubeClass()

proxy = CachedYoutubeClass(youtube_service)

manager = YoutubeManager(proxy)

manager.react_on_user_input()