class User:
    def __init__(self, nickname, rating=0, posts=0, comments=0):
        self.nickname=nickname
        if rating<0:
            print (self.nickname+ ", Rating cannot be less than zero. Rating set to ZERO!")
            self.rating=0
        elif rating>5:
            print (self.nickname+ ", ERROR! Rating caanot be more than 5. Rating set to ZERO!")
            self.rating=0
        else:
            self.rating=rating

        if posts<0:
            print (self.nickname+ ", Number of posts cannot be less than ZERO. Parameter set to ZERO!")
            self.posts=0
        else:
            self.posts=posts

        if comments<0:
            print (self.nickname+ ", Number of comments cannot be less than ZERO. Parameter set to ZERO!")
            self.comments=0
        else:
            self.comments=comments            

    def __str__ (self):
        return f'{self.nickname}, rating = {self.rating}, posts = {self.posts}, comments = {self.comments}'        
    
    def like (self):
        if self.rating>=5:
            self.rating=5
        else:    
            self.rating+=1

    def dislike (self):
        if self.rating<=0:
            self.rating=0
        else:
            self.rating-=1

    def comment (self):
        self.comments+=1

    def post (self):
        self.posts+=1


print ()
user1=User("John", 3, -1, -1)
print (user1)

user1.like()
user1.dislike()
user1.post()
user1.comment()
user1.comment()
user1.post()
print (user1)

        