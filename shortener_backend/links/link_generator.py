import random
import string


class LinkGenerator:
    def __init__(self, domain_url: str, link_path_len: int):
        self.domain_url: str = domain_url
        self.link_path_len: int = link_path_len
        self.link_path: str = ""
        self.full_link: str = ""

    def run(self) -> None:
        path: str = self.generate_random_link_path()
        self.link_path = path
        self.full_link = self.domain_url + path

    def generate_random_link_path(self) -> str:
        characters: str = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(self.link_path_len))
