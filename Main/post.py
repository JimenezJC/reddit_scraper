class Post(object):
    """This class is for the Post objects

        Attributes:
            title: A String object that holds the title of the post
            comments: is an integer that holds the amount of comments made in
                      the post
            timeSubmitted: a datetime object that tracks the date and time the
                           post was created
            link: A string that holds the link to the comments of the post

    """

    def __init__(self,title,user,comments,timeSubmitted, link, commentsLink):
        self.title = title
        self.comments = comments
        self.timeSubmitted = timeSubmitted
        self.link = link
        self.commentsLink = commentsLink




class PostList(object):
    """This is a class that will run queries on Posts objects

        Attributes:
            posts: An array that holds all Post objects
            size: The amount of posts inside the array
            search: String that holds the search query for this postlist

    """

    def __init__(self,search, posts = []):
        self.search = search
        self.posts = posts
        self.size = len(posts)

    def add(self, post):
        self.posts.append(post)


    def addFromList(self, postList):
        self.posts.extend(postList.posts)