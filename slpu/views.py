import datetime

from django.shortcuts import render
from django.db.models import Count, Sum, Value
# from django.db.models.functions import Concat

from .models import SLpu
from .models import XmlSchet
from .models import XmlUsl
from .models import Sankc


def slpu(request):

    slpu_all = SLpu.objects.all().count()
    slpu_g = SLpu.objects.values("glpu").annotate(Count('glpu')).count()

    all_slpu = SLpu.objects.values("glpu", "mcod", "name").filter(
        mcod__in=SLpu.objects.values("glpu").distinct()
    ).order_by('glpu', 'mcod')

    slpu_1 = SLpu.objects.filter(idump=1).count()
    slpu_2 = SLpu.objects.filter(idump=2).count()
    slpu_3 = SLpu.objects.filter(idump=3).count()
    slpu_4 = SLpu.objects.filter(idump=4).count()
    slpu_5 = SLpu.objects.filter(idump=5).count()
    slpu_6 = SLpu.objects.filter(idump=6).count()

    cnt = {
        'все МО': slpu_g,
        'все с подрз.': slpu_all,
        'стац.': slpu_1,
        'дн.стац.': slpu_2,
        'пол.': slpu_3,
        'ск.пом.': slpu_4,
        'стом.': slpu_5,
        'диагн.': slpu_6,
    }

    mdt = {
        'all_slpu' : all_slpu,
        'cnt' : cnt,
    }

    return render(request, 'slpu.html', mdt)


def glpu_data(request, glpuid):
    slpu_mo = SLpu.objects.raw("SELECT sl.GLPU, sl.MCOD, sl.NAME, sl.IDUMP, u.UMPNAME "
                               "FROM S_LPU sl "
                               "LEFT JOIN USLMP u "
                               "ON sl.IDUMP = u.IDUMP "
                               "WHERE sl.GLPU = %s "
                               "ORDER BY sl.MCOD", (glpuid,))

    gl_slpu = SLpu.objects.values("glpu", "m_namef").filter(mcod=glpuid)

    all_period = XmlSchet.objects.\
        values("glpu", "mont", "yer", "period").\
        distinct().filter(glpu=glpuid).order_by("yer", "mont")

    # all_period = AllFiles.objects.raw('SELECT DISTINCT af.GLPU, af.MONTH, af.YEAR, '
    #                                   'af.MONTH || af.YEAR period '
    #                                   'FROM ALL_FILES af '
    #                                   'WHERE af.GLPU = %s '
    #                                   'ORDER BY af.YEAR, af.MONTH', (glpuid,))

    data_ut = {}
    for period in all_period:
        dt_ut = datetime.datetime.strptime(period['period'], '%d.%m.%Y')
        ut = XmlUsl.objects.filter(lpu=glpuid, period=dt_ut).\
                aggregate(sumv=Sum('sumv_usl'), cnt=Count('*'))
        snk = Sankc.objects.filter(glpu=glpuid, period=period['period']).\
                aggregate(sumsnk=Sum('summ_shtr'), snkcnt=Count('*'))
        ut.update({'sumsnk' : 0.00, 'snkcnt' : 0} if snk['sumsnk'] is None else snk)
        data_ut[period['period'].replace('.', '')[2:]] = ut

    res = {
        'glpu' : gl_slpu[0]['glpu'],
        'slpumo' : slpu_mo,
        'glslpu' : gl_slpu,
        'data_ut' : data_ut,
    }

    return render(request, 'slpumo.html', res)


def infomcod(request, glpuid, mcodid):
    gl_slpu = SLpu.objects.values("glpu", "m_namef").filter(mcod=glpuid)
    mc_slpu = SLpu.objects.raw("SELECT sl.*, u.UMPNAME "
                               "FROM S_LPU sl "
                               "LEFT JOIN USLMP u "
                               "ON sl.IDUMP = u.IDUMP "
                               "WHERE sl.mcod = %s", (mcodid,))

    res = {
        'glslpu': gl_slpu,
        'mcslpu' : mc_slpu,
    }

    return render(request, 'mcoddata.html', res)


def eksp(request, glpuid, period):
    exp_date = '01.'+period[0:2]+'.'+period[2:]
    gl_slpu = SLpu.objects.values("glpu", "m_namef").filter(mcod=glpuid)

    cnt_err = Sankc.objects.filter(glpu=glpuid, period=exp_date). \
        aggregate(sumsnk=Sum('summ_shtr'), snkcnt=Count('*'))

    lpu_eks = Sankc.objects.raw("SELECT s.*, xp.FAM||' '||xp.IM||' '||xp.OT fio, xp.DR, xp.ADRES "
                                "FROM SANKC s "
                                "LEFT JOIN XML_PACIENT PARTITION(p{}) xp "
                                "ON s.GLPU = xp.GLPU AND s.ID_PAC = xp.ID_PAC "                               
                                "WHERE s.GLPU = %s AND s.PERIOD = %s "
                                "ORDER BY fio".format(period[0:2]+period[2:]), (glpuid, exp_date))
    res = {
        'period' : 'Месяц: '+period[0:2]+' Год: '+period[2:],
        'cnt_err' : cnt_err,
        'glslpu': gl_slpu,
        'eks' : lpu_eks,
    }
    return render(request, 'slpu_exp.html', res)
