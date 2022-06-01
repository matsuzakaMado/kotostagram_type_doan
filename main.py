import random
import argparse

from credentials import ACTIVE_FOLLOWEE,MAX_FOLLOW_COUNT,MAX_LIKE_COUNT,LIKE_COUNT_FOR_KEY,KEYWORDS
from instagram import Instagram
from utils import init_loggers


if __name__ == '__main__':
    init_loggers()

    # IDとpasswordをコマンドライン引数から取得する
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    parser.add_argument('password')
    # コマンドライン引数を解析する
    account = parser.parse_args()

    # Instagramオブジェクトを作成する
    instagram = Instagram()

    # ログイン
    instagram.login(account.id, account.password)
   
    # 有効フォロウィーのアカウントを取得(後程、dbから取得するよう変更)
    active_followee = ACTIVE_FOLLOWEE
    # 合計でフォローした人数を入れる変数を定義
    follow_cnt_sum = 0

    # フォロー機能1
    # フォロー機能1でフォローする人数を設定
    print('フォロー機能1を開始します')
    max_follow_count1 = 15 # 任意に変更
    random.shuffle(active_followee)
    follow_cnt1 = 0 # フォロー機能1でフォローした人数
    max_follow_cnt1_by_parent = max_follow_count1
    # フォローした人数がmax_count1人を超えるまでフォロー処理1を繰り返す
    for parent_account in active_followee:
        print(parent_account)
        try:
            # フォローを行い、フォローした人数を加える
            follow_cnt1 += instagram.follow1(parent_account, max_follow_cnt1_by_parent)
        except Exception:
            pass
        # エラーになる前にフォローした人数は確実に加えなければならない
        if follow_cnt1 >= max_follow_count1 :
            break
        max_follow_cnt1_by_parent = max_follow_count1 - follow_cnt1
    follow_cnt_sum += follow_cnt1
    print('フォロー機能1で予定人数{sch}人中、{follow}人フォローしました' .format(sch=max_follow_count1, follow=follow_cnt1))
    print('現在までで、最大人数{max}人中、合計{sum}人フォローしました' .format(max=MAX_FOLLOW_COUNT, sum=follow_cnt_sum))
    print('フォロー機能1を終了します')


    #フォロー機能2
    # フォロー機能2でフォローする人数を設定
    print('フォロー機能2を開始します')
    max_follow_count2 = MAX_FOLLOW_COUNT - follow_cnt1 # 任意に変更
    random.shuffle(active_followee)
    follow_cnt2 = 0 # フォロー機能2でフォローした人数
    max_follow_cnt2_by_parent = max_follow_count2
    # フォローした人数がmax_count2人を超えるまでフォロー処理2を繰り返す
    for parent_account in active_followee:
        print(parent_account)
        try:
            # フォローを行い、フォローした人数を加える
            follow_cnt2 += instagram.follow2(parent_account, max_follow_cnt2_by_parent)
        except Exception:
            pass
        # フォローした人数が規定数に達した場合、処理を抜ける
        if follow_cnt2 >= max_follow_count2 :
            break
        max_follow_cnt2_by_parent = max_follow_count2 - follow_cnt2
    follow_cnt_sum += follow_cnt2
    print('フォロー機能2で予定人数{sch}人中、{follow}人フォローしました' .format(sch=max_follow_count2, follow=follow_cnt2))
    print('現在までで、最大人数{max}人中、合計{sum}人フォローしました' .format(max=MAX_FOLLOW_COUNT, sum=follow_cnt_sum))
    print('フォロー機能2を終了します')
    
    #いいね機能
    # いいね機能1でいいねする数を設定
    max_like_count = MAX_LIKE_COUNT
    max_like1_count = MAX_LIKE_COUNT # 任意に変更
    cnt = LIKE_COUNT_FOR_KEY
    # いいね機能1で検索するキーワードを設定
    keywords = KEYWORDS

    for key in keywords:
        # キーワードごとにいいねした数を設定
        like_count_for_key = 0
        like_count_for_key += instagram.like1(key, max_like1_count, cnt)
        if like_count_for_key >= max_like1_count:
            break
        max_like1_count = max_like1_count - like_count_for_key
        #時間があればガベージコレクションとlikeを30件は必ずするというようなことを行いたい。あとpasswordとidはまた取得しなおしたい。
        #ブラウザを閉じるところまで行いたい
