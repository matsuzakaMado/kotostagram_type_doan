from time import sleep
from drivers import Driver

class SeleniumLib(Driver):
    def __init__(self):
        super(SeleniumLib, self).__init__()
        self.page = None

    #インスタグラムにログインを行う
    def login(self, id, password):
        try:
            #インスタグラムにアクセス
            self.get('https://www.instagram.com/accounts/login/')
            sleep(3)
            #ログインフォームを探し、入力する。
            sign_box = self.find_element_by_tag_name('form')
            sign_box.find_element_by_name('username').send_keys(id)
            sign_box.find_element_by_name('password').send_keys(password)
            #ログインボタン押下
            login_btn = sign_box.find_element_by_xpath('//button[@type="submit"]')
            login_btn.click()
            print('login succeeded')
            sleep(3)
            #ダイアログを閉じる
            dialog_box = self.find_element_by_xpath('//div[@role="dialog"]')
            btn = dialog_box.find_element_by_tag_name('button')
            btn.click()
            print('login_succeeded')
        except Exception:
            pass

    #特定のキーワードで検索を行い、最新の投稿cnt件のurlを取得
    def search(self, keyword, cnt):
        self.get('https://www.instagram.com/explore/tags/{}/'.format(keyword))
        sleep(10)#検索には時間がかかるため、ここはwebdriverを用いたい10秒でも結構ぎり
        articles = self.find_element_by_tag_name('main').find_element_by_tag_name('article').find_elements_by_tag_name('a')
        links = []
        i=0
        for article in articles:
            links.append(article.get_attribute('href'))
            i = i+1
            if i>=cnt:
                print('記事URL{}件取得' .format(i))
                return links
        print('記事が規定数を満たしませんでした。記事数：{}件' .format(i))
        return links

    #プロフィール画面上でフォローを行う
    def follow(self):
        main = self.find_element_by_tag_name('main').find_element_by_tag_name('header')
        try:
            button = main.find_element_by_xpath('//button[normalize-space()="フォローする"]')
            button.click()
            print('follow succeeded')
            return 1
        except:
            print('follow faild')
            return 0

    def like(self, url):
        self.get(url)
        sleep(10)#ここはちょっと考える
        # ターゲット検索
        elem_target_nice_text = self.find_elements_by_class_name('_8-yf5')
        # いいねフラグ
        like_flg = 0

        sleep(3)
        # いいね処理
        for e in elem_target_nice_text:
            if e.get_attribute('aria-label') != 'いいね！' :
                return like_flg
            else:
                self.find_element_by_class_name('fr66n').click()
                like_flg = 1
        return like_flg


    #プロフィール画面に移動(引数:アカウント名)
    def show_profile_page(self, id):
        self.get('https://www.instagram.com/{}/'.format(id))