# coding: utf-8

from .abs_analyzer import AbsAnalyzer
import datetime
import pandas as pd

##################################################
# 鉄道の解析クラス。
##################################################
class RailroadAnalyzer(AbsAnalyzer):
    """ 鉄道の解析クラス。
        
    Attributes:
        _base_dir (string)      : ベースディレクトリ
        _ouput_dirname (string) : 出力ディレクトリ名
        _ouput_dir (string)     : 出力ディレクトリパス
    """
    
    ##################################################
    # コンストラクタ
    ##################################################
    def __init__(self, base_dir, ouput_dirname):
        """ コンストラクタ。
        
        Args:
            base_dir (string)       : ベースディレクトリ
            ouput_dirname (string)  : 出力ディレクトリ名
        Returns:
        """
        
        # 抽象クラスのコンストラクタ
        super().__init__(base_dir, ouput_dirname)
        
    ##################################################
    # 証券コードと名称のディクショナリを返す。
    ##################################################
    def _get_codes(self):
        """ 証券コードと名称のディクショナリを返す。
        
        Args:
        Returns:
            dict    : 証券コードと名称のディクショナリ
                        (ex){'JR東日本':9020, 'JR西日本': 9021}
        """
        
        codes = {
            'JR東日本'  : 9020, 
            'JR東海'    : 9022, 
            'JR西日本'  : 9021, 
            'JR九州'    : 9142, 
            '東急'      : 9005, 
            '東武鉄道'  : 9001, 
            '近鉄'      : 9041,
            '阪急阪神'  : 9042,
            '名古屋鉄道': 9048,
            '西日本鉄道': 9031,
        }
        
        return codes
        
    ##################################################
    # 株価取得の範囲(開始年, 終了年)を取得する
    ##################################################
    def _get_date_range_for_stock_price(self):
        """ 株価取得の範囲(開始年, 終了年)を取得する
        
        Args:
        Returns:
            tuple   : 開始年, 終了年
        """
        return (2016, 2020)
    
    ##################################################
    # 値上がり率の基準とする日付を取得する。
    ##################################################
    def _get_ref_date_for_price_rates(self):
        """ 値上がり率の基準とする日付を取得する。
        
        Args:
        Returns:
            datetime    : 値上がり率の基準とする日付
                          Noneの場合は最旧日付になる
        """
        return None
    
    ##################################################
    # 株価チャート表示開始日付を取得する。
    ##################################################
    def _get_stock_chart_start_date(self):
        """ 株価チャート表示開始日付を取得する。
        
        Args:
        Returns:
            string  : 株価チャート表示開始日付を下記形式の文字列で返す。
                        (ex) 'YYYY-MM-DD'
        """
        return '2020-01-01'
        
    ##################################################
    # 株価を補正する。
    ##################################################
    def _correct_stock_prices(self, df):
        """ 株価を補正する。
            株式分割や併合に対する補正として使用する。
        Args:
            df(DataFrame)   : 株価データが格納されたDataFrame
        Returns:
            DataFrame   : 補正後のDataFrame
        """
        
        new_df = df.copy()
        
        # 東武鉄道の株式併合(2017/09/27)に対する補正
        new_df.loc[pd.IndexSlice['東武鉄道', :'2017-09-26'],'終値'] *= 5
        
        # 東急の株式併合(2017/07/27)に対する補正
        new_df.loc[pd.IndexSlice['東急', :'2017-07-26'],'終値'] *= 2
        
        # 西日本鉄道の株式併合(2017/09/27)に対する補正
        new_df.loc[pd.IndexSlice['西日本鉄道', :'2017-09-26'],'終値'] *= 5
        
        # 阪急阪神の株式併合(2017/07/27)に対する補正
        new_df.loc[pd.IndexSlice['阪急阪神', :'2016-07-26'],'終値'] *= 5
        
        # 近鉄の株式併合(2017/09/27)に対する補正
        new_df.loc[pd.IndexSlice['近鉄', :'2017-09-26'],'終値'] *= 10
        
        # 名古屋鉄道の株式併合(2017/09/27)に対する補正
        new_df.loc[pd.IndexSlice['名古屋鉄道', :'2017-09-26'],'終値'] *= 5
        
        
        return new_df
        