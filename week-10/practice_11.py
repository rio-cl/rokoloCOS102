class Nigeria():
    def capital(self):
        print("Lagos is the capital of Nigeria.")

    def language(self):
        print("English is the official language of Nigeria.")

    def type(self):
        print("Nigeria is the giant of Africa.")


class Togo():
    def capital(self):
        print("Lome is the capital of Togo.")

    def language(self):
        print("French is the primary language of Togo.")


    def type(self):
        print("Togo is known for its palm-lined beaches and hilltop villages.")


obj_naija = Nigeria()
obj_togo = Togo()
for country in (obj_naija, obj_togo):
    country.capital()
    country.language()
    country.type()
