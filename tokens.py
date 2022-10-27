class Token:
    def __init__(self,token,Lexema):
        self.token=token
        self.lexema=Lexema

    def toString(self):
        return f"====Token===\ntoken: {self.token}\nlexema: {self.lexema}"