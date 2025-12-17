class BaseService[R]:
    def __init__(self, repo: R) -> None:
        self.repo = repo
