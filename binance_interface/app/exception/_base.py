class AbstractEXP(Exception):
    error_msg: str

    def __str__(self):
        return self.error_msg
