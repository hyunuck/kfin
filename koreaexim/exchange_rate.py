
class ExchangeRate:
    def __init__(self, result, cur_unit, ttb, tts, deal_bas_r, bkpr, yy_efee_r, ten_dd_efee_r, kftc_bkpr, kftc_deal_bas_r, cur_nm):
        self.result = result
        self.cur_unit = cur_unit
        self.ttb = ttb
        self.tts = tts
        self.deal_bas_r = deal_bas_r
        self.bkpr = bkpr
        self.yy_efee_r = yy_efee_r
        self.ten_dd_efee_r = ten_dd_efee_r
        self.kftc_bkpr = kftc_bkpr
        self.kftc_deal_bas_r = kftc_deal_bas_r
        self.cur_nm = cur_nm

    def __str__(self):
        return f"{self.cur_nm} ({self.cur_unit}): TTB={self.ttb}, TTS={self.tts}"

    @classmethod
    def from_dict(cls, d):
        return cls(**d)