from notice_handler.notice_builder_interface import INoticeBuilder


class Notice:
    subject: str
    year: str
    date: str
    title: str
    content: str
    attachment_text: str
    attachment_link: str


class NoticeBuilder(INoticeBuilder):
    _notice: Notice

    def __init__(self) -> None:
        """
        A new builder instance should contain a blank notice object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._notice = Notice()

    @property
    def notice(self) -> Notice:
        """
        Method used to retrieving result.

        After returning the end result to the client, a builder
        instance will be ready to start producing another notice.
        """
        notice = self._notice
        self.reset()
        return notice

    def set_subject(self, subject) -> None:
        self._notice.subject = subject

    def set_year(self, year) -> None:
        self._notice.year = year

    def set_date(self, date) -> None:
        self._notice.date = date

    def set_title(self, title) -> None:
        self._notice.title = title

    def set_content(self, content) -> None:
        self._notice.content = content

    def set_text(self, text) -> None:
        self._notice.attachment_text = text

    def set_link(self, link) -> None:
        self._notice.attachment_link = link
