from abc import ABC, abstractmethod


class INoticeBuilder(metaclass=ABC):
    """
    Notice Builder Interface
    """

    @property
    @abstractmethod
    def notice(self) -> None:
        pass

    @abstractmethod
    def set_subject(self, subject) -> None:
        pass

    @abstractmethod
    def set_year(self, year) -> None:
        pass

    @abstractmethod
    def set_date(self, date) -> None:
        pass

    @abstractmethod
    def set_title(self, title) -> None:
        pass

    @abstractmethod
    def set_content(self, content) -> None:
        pass

    @abstractmethod
    def set_text(self, text) -> None:
        pass

    @abstractmethod
    def set_link(self, link) -> None:
        pass
