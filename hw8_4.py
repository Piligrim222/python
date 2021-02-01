class Sklad:
    pass


class Orgtehnika:
    def __init__(self, kolichestvo):
        self.kolichestvo = kolichestvo

    def sozdanie(self):
        return self.kolichestvo


class Printer(Orgtehnika):
    pass


class Skaner(Orgtehnika):
    pass


class Kseroks(Orgtehnika):
    pass

