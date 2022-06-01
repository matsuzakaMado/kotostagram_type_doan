import instaloader

class InstaloaderLib():
    def __init__(self):
        self.loader = instaloader.Instaloader()

    def login(self, id, password):
        self.loader.login(id, password)
        print('login succeeded')

    #フォロワーを取得(引数：アカウント名)
    #全件取得ではなく上から二番目とか、100件上からとかできないかなぁ。あとフォローしていないとか。後そんなに早くはない。
    def get_followers(self, id):
        #指定したIDのフォロワーを全件取得
        profile = instaloader.Profile.from_username(self.loader.context, id)
        i = 0
        followers = []
        for follower in profile.get_followers():
            followers.append(follower.username)
        return followers

    #最新投稿にいいねしたアカウントを取得
    def get_like_accounts(self, id):
        profile = instaloader.Profile.from_username(self.loader.context, id)
        posts = profile.get_posts()
        i = iter(posts)
        post = next(i)
        like_accounts = []
        for user in post.get_likes():
            like_accounts.append(user.username)
        return like_accounts