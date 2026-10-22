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

        if uzivatele is None:
            return None

        if uzivatele.over_heslo(password):
            return uzivatele

        return None

    def najdi_uzivatele_id(self,id):
        for uzivatel in self.uzivatele:
            if uzivatel.id == id:
                return uzivatel
        return None