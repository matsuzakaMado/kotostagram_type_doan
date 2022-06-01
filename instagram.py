import random

from instaloader_lib import InstaloaderLib
from selenium_lib import SeleniumLib

#IDとpasswordを定義
class Instagram:
    def __init__(self):
        self.L = InstaloaderLib()
        self.S = SeleniumLib()

    #インスタグラムにログインを行う
    def login(self, INSTAGRAM_ID, INSTAGRAM_PASSWORD):
        self.L.login(INSTAGRAM_ID, INSTAGRAM_PASSWORD)
        self.S.login(INSTAGRAM_ID, INSTAGRAM_PASSWORD)

    # フォロー機能1
    def follow1(self, parent_id, max_count):
        #有効フォロウィーのフォロワーを取得(ランダムに並び替える)
        followers = self.L.get_followers(parent_id)
        random.shuffle(followers)

        # フォローした人数を定義
        follow_cnt = 0

        #フォローをフォロー人数max_countまたはEOFまで繰り返す
        for user in followers:
            # プロフィールに移動
            self.S.show_profile_page(user)
            # フォロー(フォローしていない、かつ、フォロワーにいない場合)
            follow_cnt += self.S.follow()
            # フォローした人数がmax_countになれば繰り返しを抜ける
            if follow_cnt == max_count:
                print("規定人数に達しました")
                return follow_cnt
            else :
                print("continue")
        else:
            print("規定人数に満ちませんでした")
        # フォローした人数を返す
        return follow_cnt
            


    # フォロー機能2
    def follow2(self, parent_id, max_count):
        # 有効フォロウィーの最新の投稿にいいねしたアカウントを取得
        like_accounts = self.L.get_like_accounts(parent_id)
    
        # フォローした人数を定義
        follow_cnt = 0
        # フォローをフォロー人数max_countまたはEOFまで繰り返す
        for user in like_accounts:
            # プロフィールに移動
            self.S.show_profile_page(user)
            # フォロー(フォローしていない、かつ、フォロワーにいない場合)
            follow_cnt += self.S.follow()
            # フォローした人数がmax_countになれば繰り返しを抜ける
            if follow_cnt == max_count:
                print("規定人数に達しました")
                return follow_cnt
            else:
                print("continue")
        else:
            print("規定人数に満ちませんでした")
        # フォローした人数を返す
        return follow_cnt

    # いいね機能1
    def like1(self, keyword, max_count, cnt):
        # 検索して、最新の投稿cnt件のurlを取得する
        articles = self.S.search(keyword, cnt)
        # いいねした件数を設定
        like_count = 0
        # 最新の投稿にcnt件いいねする
        for url in articles:
            try:
                like_count += self.S.like(url)
            except:
                pass
            if like_count >= cnt:
                print('規定いいね数に達しました')
                return like_count
            if like_count >= max_count:
                print('最大いいね数に達しました')
                return like_count
        return like_count
