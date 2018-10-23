from applications.camps.models import Camp
from applications.camps.models import CamperInCamp
from applications.campers.models import Camper

camps = Camp.objects.filter(start__year__gte = '2016')

for camp in camps:

    age1 = 0
    age2 = 0
    age3 = 0
    age4 = 0
    camp_in_camper = CamperInCamp.objects.filter(camp = camp.id)

    for cp_cr in camp_in_camper:
        #print(cp_cr.camper)
        camper = Camper.objects.get(id= cp_cr.camper.id)

        if (camper.birthday.year >= 2013):
            age1 += 1
        if ((camper.birthday.year >= 2006) and (camper.birthday.year <= 2012)):
            age2 += 1
        if ((camper.birthday.year >= 2001) and (camper.birthday.year<= 2005)):
            age3 += 1
        if (camper.birthday.year <= 2005):
            age4 += 1

    total_campers = age1 + age2 + age3 + age4

    if total_campers != 0:

        print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            camp.id,
            camp.name,
            camp.start.date(),
            camp.end.date(),
            camp.school,
            total_campers,
            age1,
            age2,
            age3,
            age4
        ))


