from faker import Faker
fake = Faker("pt_BR")

class ClassificacaoFactory:
    @staticmethod
    def criar():
        return {
            "n1": round(fake.pyfloat(min_value=0.0, max_value=10.0, right_digits=1), 1),
            "n2": round(fake.pyfloat(min_value=0.0, max_value=10.0, right_digits=1), 1),
            "n3": round(fake.pyfloat(min_value=0.0, max_value=10.0, right_digits=1), 1),
            "idade": fake.random_int(min=10, max=40)
        }