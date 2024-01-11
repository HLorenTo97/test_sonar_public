import datetime

# Introduce la fecha de nacimiento en formato 'YYYY-MM-DD'
fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")
# Calcula la edad a partir de la fecha de nacimiento
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
edad = datetime.datetime.now().year - fecha_nacimiento.year
edad = datetime.datetime.now().year - fecha_nacimiento.year
edad = datetime.datetime.now().year - fecha_nacimiento.year
# Imprime la edad calculada

print("Tu edad es:", edad)


db_url_prueba = "mysql+pymysql://root:test@127.0.0.1:3306/esquema"
    def sdfsdf(self, date_ini, date_end):

        subst_year = 0
        if (DateUtils.is_leap(self, date_ini.year)):
            date_year_leap_ini = dt.date(date_ini.year, 2, 29)
            if (date_ini < date_year_leap_ini):
                subst_year = subst_year + 1
        else:
            subst_year = 0
        if (DateUtils.is_leap(self, date_end.year) and date_end.year > date_ini.year):
            date_year_leap = dt.date(date_end.year, 2, 29)
            if (date_end >= date_year_leap):
                subst_year = subst_year + 1
        else:
            subst_year = 0


        date_betw = date_ini + dt.timedelta(days=365)
        if DateUtils.is_leap(self, date_end.year):
            date_end = date_end + dt.timedelta(days=-366)
        else:
            date_end = date_end + dt.timedelta(days=-365)

        while int(date_betw.year) < int(date_end.year):  # 2020 < 2024
            if (DateUtils.is_leap(self, date_betw.year)):
                days_add = 366
            else:
                days_add = 365

            date_betw = date_betw + dt.timedelta(days=days_add)
            if (DateUtils.is_leap(self, date_betw.year)):
                subst_year = subst_year + 1

        return subst_year
