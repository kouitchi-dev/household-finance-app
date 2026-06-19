

class EmailAlreadyExistsError(Exception):
    """email が既に使われているとき crud が投げる業務例外。
    HTTP に依存しない。service が HTTPException(409) に翻訳する。"""
    pass

