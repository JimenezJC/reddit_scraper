class SubReddit(object):
    """
        This is a class for the SubReddit Objects

        Attributes:
            title: A string that holds the title of the subreddit
            subscribers: An integer that holds the number of accounts subscribed

    """
    def __init__(self, title, subscribers):
        self.title = title
        self.subscribers = subscribers
