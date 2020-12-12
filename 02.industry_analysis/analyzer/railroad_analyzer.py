# coding: utf-8

from .abs_analyzer import AbsAnalyzer

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
    def get_codes(self):
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
        

