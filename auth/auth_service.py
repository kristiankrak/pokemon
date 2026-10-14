class authService:
    def __init__(self,uzivatele):
        self.uzivatele = uzivatele


    def najdi_uzivatele(self,email):
        for uzivatel in self.uzivatele:
            if uzivatel.email == email:
                return uzivatel
        return None

    def prihlas(self,email,password):
        uzivatele = self.najdi_uzivatele(email)

        if uzivatele is None
            return None
