# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllFiles(models.Model):
    date_in = models.DateField(blank=True, null=True)
    glpu = models.CharField(max_length=12)
    priz = models.CharField(max_length=2)
    year = models.CharField(max_length=8)
    month = models.CharField(max_length=4)
    date_out = models.DateField()

    class Meta:
        managed = False
        db_table = 'all_files'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Filial(models.Model):
    kfil = models.CharField(primary_key=True, max_length=4)
    naim = models.CharField(max_length=20, blank=True, null=True)
    adres = models.CharField(max_length=30, blank=True, null=True)
    nasel = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filial'


class Hediag(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    diag = models.CharField(max_length=100, blank=True, null=True)
    sex = models.NullBooleanField()
    baz = models.NullBooleanField()
    terr = models.NullBooleanField()
    comment = models.CharField(max_length=20, blank=True, null=True)
    celevka = models.CharField(max_length=2, blank=True, null=True)
    chkmrk = models.CharField(max_length=2, blank=True, null=True)
    note = models.CharField(max_length=2, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    compr = models.CharField(max_length=4, blank=True, null=True)
    b_age = models.IntegerField(blank=True, null=True)
    b_compr = models.CharField(max_length=4, blank=True, null=True)
    t_age = models.IntegerField(blank=True, null=True)
    t_compr = models.CharField(max_length=4, blank=True, null=True)
    d_osl = models.NullBooleanField()
    iz = models.CharField(max_length=20, blank=True, null=True)
    sex_do = models.NullBooleanField()
    terr_do = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'hediag'


class Help(models.Model):
    topic = models.CharField(primary_key=True, max_length=50)
    seq = models.BigIntegerField()
    info = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help'
        unique_together = (('topic', 'seq'),)


class Podush(models.Model):
    glpu = models.CharField(max_length=6, blank=True, null=True)
    smo = models.CharField(max_length=5, blank=True, null=True)
    ot_god = models.IntegerField(blank=True, null=True)
    ot_mes = models.IntegerField(blank=True, null=True)
    sump = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'podush'


class SLpu(models.Model):
    mcod = models.CharField(primary_key=True, max_length=6)
    id = models.BigIntegerField(blank=True, null=True)
    glpu = models.CharField(max_length=6, blank=True, null=True)
    tf_okato = models.CharField(max_length=5, blank=True, null=True)
    typ = models.BigIntegerField(blank=True, null=True)
    idsp = models.BigIntegerField(blank=True, null=True)
    idump = models.BigIntegerField(blank=True, null=True)
    krai = models.CharField(max_length=3, blank=True, null=True)
    urop = models.BigIntegerField(blank=True, null=True)
    smo = models.CharField(max_length=10, blank=True, null=True)
    pit = models.BigIntegerField(blank=True, null=True)
    ur_gr = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    m_ogrn = models.CharField(max_length=15, blank=True, null=True)
    m_namef = models.CharField(max_length=250, blank=True, null=True)
    m_post = models.CharField(max_length=6, blank=True, null=True)
    m_parent = models.BigIntegerField(blank=True, null=True)
    m_parent1 = models.CharField(max_length=30, blank=True, null=True)
    m_org = models.BigIntegerField(blank=True, null=True)
    mpost_id = models.CharField(max_length=6, blank=True, null=True)
    m_adres = models.CharField(max_length=250, blank=True, null=True)
    fam_gv = models.CharField(max_length=40, blank=True, null=True)
    im_gv = models.CharField(max_length=40, blank=True, null=True)
    ot_gv = models.CharField(max_length=40, blank=True, null=True)
    fam_buh = models.CharField(max_length=40, blank=True, null=True)
    im_buh = models.CharField(max_length=40, blank=True, null=True)
    ot_buh = models.CharField(max_length=40, blank=True, null=True)
    tel = models.CharField(max_length=40, blank=True, null=True)
    tel_reg = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    e_mail = models.CharField(max_length=30, blank=True, null=True)
    date_b = models.DateField(blank=True, null=True)
    date_e = models.DateField(blank=True, null=True)
    date_red = models.DateField(blank=True, null=True)
    m_inn = models.CharField(max_length=12, blank=True, null=True)
    m_kpp = models.CharField(max_length=9, blank=True, null=True)
    m_okpo = models.CharField(max_length=8, blank=True, null=True)
    m_okved = models.CharField(max_length=8, blank=True, null=True)
    m_okopf = models.CharField(max_length=2, blank=True, null=True)
    m_fs = models.BigIntegerField(blank=True, null=True)
    md_start = models.DateField(blank=True, null=True)
    md_end = models.DateField(blank=True, null=True)
    u_mp = models.BigIntegerField(blank=True, null=True)
    ht_mp = models.BigIntegerField(blank=True, null=True)
    sp_mp = models.BigIntegerField(blank=True, null=True)
    skor_mp = models.BigIntegerField(blank=True, null=True)
    avia_mp = models.BigIntegerField(blank=True, null=True)
    nor_pay = models.BigIntegerField(blank=True, null=True)
    fs_pay = models.BigIntegerField(blank=True, null=True)
    m_out = models.BigIntegerField(blank=True, null=True)
    pay_work = models.BigIntegerField(blank=True, null=True)
    m_np1 = models.BigIntegerField(blank=True, null=True)
    m_np2 = models.BigIntegerField(blank=True, null=True)
    m_np3 = models.BigIntegerField(blank=True, null=True)
    du = models.BigIntegerField(blank=True, null=True)
    tss = models.FloatField(blank=True, null=True)
    knum = models.BigIntegerField(blank=True, null=True)
    procdstacp = models.BigIntegerField(blank=True, null=True)
    stoms = models.BigIntegerField(blank=True, null=True)
    om_name = models.CharField(max_length=250, blank=True, null=True)
    om_primec = models.CharField(max_length=250, blank=True, null=True)
    om_dogovor = models.CharField(max_length=250, blank=True, null=True)
    om_nomerli = models.CharField(max_length=50, blank=True, null=True)
    om_datebeg = models.DateField(blank=True, null=True)
    om_dateend = models.DateField(blank=True, null=True)
    dostup = models.FloatField(blank=True, null=True)
    reenom = models.CharField(max_length=6, blank=True, null=True)
    id_exp = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_lpu'


class Sankc(models.Model):
    glpu = models.CharField(max_length=12)
    mcod = models.CharField(max_length=12, blank=True, null=True)
    povod = models.CharField(max_length=30, blank=True, null=True)
    flag = models.BigIntegerField(blank=True, null=True)
    id_pac = models.CharField(max_length=72, blank=True, null=True)
    id_sluch = models.CharField(max_length=76)
    idserv = models.CharField(primary_key=True, max_length=76)
    id_user = models.CharField(max_length=20, blank=True, null=True)
    date_exp = models.DateField(blank=True, null=True)
    period = models.CharField(max_length=12)
    comments = models.CharField(max_length=100, blank=True, null=True)
    summ_shtr = models.FloatField(blank=True, null=True)
    label = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sankc'
        unique_together = (('idserv', 'period', 'id_sluch', 'glpu'),)


class Smp(models.Model):
    ecoklpu = models.CharField(max_length=7, blank=True, null=True)
    glpu = models.CharField(max_length=6, blank=True, null=True)
    sum = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=2, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    data = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smp'


class SpTarif(models.Model):
    ur = models.FloatField(blank=True, null=True)
    vozr = models.FloatField(blank=True, null=True)
    name_issl = models.CharField(max_length=255, blank=True, null=True)
    ksg = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    sr_preb = models.FloatField(blank=True, null=True)
    idpr = models.FloatField(blank=True, null=True)
    kdprice = models.FloatField(blank=True, null=True)
    idump = models.FloatField(blank=True, null=True)
    nozol = models.CharField(max_length=255, blank=True, null=True)
    kol_usl = models.FloatField(blank=True, null=True)
    t_type = models.FloatField(blank=True, null=True)
    intp = models.FloatField(blank=True, null=True)
    idvmp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tarif'


class Uet(models.Model):
    kod = models.CharField(max_length=2, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    dat2 = models.DateField(blank=True, null=True)
    koef = models.FloatField(blank=True, null=True)
    num = models.NullBooleanField()
    pos = models.FloatField(blank=True, null=True)
    ort = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uet'


class Uslmp(models.Model):
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    idump = models.IntegerField(blank=True, null=True)
    umpname = models.CharField(max_length=30, blank=True, null=True)
    maks_idump = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uslmp'


class VidExp(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    kod = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_exp'


class Vidmp(models.Model):
    datebeg = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    idvmp = models.IntegerField(blank=True, null=True)
    vmpname = models.CharField(max_length=254, blank=True, null=True)
    idump = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'vidmp'


class XmlHrrgd(models.Model):
    idserv = models.CharField(max_length=36)
    idnomk = models.CharField(primary_key=True, max_length=36)
    hkod = models.CharField(max_length=25, blank=True, null=True)
    name_o = models.CharField(max_length=250, blank=True, null=True)
    smo = models.CharField(max_length=5, blank=True, null=True)
    glpu = models.CharField(max_length=6, blank=True, null=True)
    mcod = models.CharField(max_length=6)
    ksgh = models.CharField(max_length=36, blank=True, null=True)
    period = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'xml_hrrgd'
        unique_together = (('idnomk', 'mcod'),)


class XmlPacient(models.Model):
    id_sch = models.CharField(max_length=25, blank=True, null=True)
    vpolis = models.BigIntegerField(blank=True, null=True)
    spolis = models.CharField(max_length=10, blank=True, null=True)
    npolis = models.CharField(max_length=20, blank=True, null=True)
    smo = models.CharField(max_length=5, blank=True, null=True)
    smo_ogrn = models.CharField(max_length=15, blank=True, null=True)
    smo_ok = models.CharField(max_length=5, blank=True, null=True)
    smo_nam = models.CharField(max_length=50, blank=True, null=True)
    novor = models.CharField(max_length=8, blank=True, null=True)
    fam = models.CharField(max_length=40, blank=True, null=True)
    im = models.CharField(max_length=40, blank=True, null=True)
    ot = models.CharField(max_length=40, blank=True, null=True)
    w = models.BigIntegerField(blank=True, null=True)
    dr = models.DateField(blank=True, null=True)
    fam_p = models.CharField(max_length=40, blank=True, null=True)
    im_p = models.CharField(max_length=40, blank=True, null=True)
    ot_p = models.CharField(max_length=40, blank=True, null=True)
    w_p = models.BigIntegerField(blank=True, null=True)
    dr_p = models.DateField(blank=True, null=True)
    mr = models.CharField(max_length=60, blank=True, null=True)
    doctype = models.BigIntegerField(blank=True, null=True)
    docser = models.CharField(max_length=10, blank=True, null=True)
    docnum = models.CharField(max_length=20, blank=True, null=True)
    snils = models.CharField(max_length=15, blank=True, null=True)
    adres = models.CharField(max_length=80, blank=True, null=True)
    stat = models.BigIntegerField(blank=True, null=True)
    polis = models.CharField(max_length=30)
    id_pac = models.CharField(max_length=36)
    vnov_d = models.CharField(max_length=10, blank=True, null=True)
    glpu = models.CharField(max_length=6)
    dost = models.CharField(max_length=10, blank=True, null=True)
    dost_p = models.CharField(max_length=10, blank=True, null=True)
    ident_sp = models.CharField(max_length=10, blank=True, null=True)
    inv = models.FloatField(blank=True, null=True)
    mse = models.FloatField(blank=True, null=True)
    period = models.DateField()

    class Meta:
        managed = False
        db_table = 'xml_pacient'


class XmlPacientExt(models.Model):
    id_pac = models.CharField(max_length=36)
    vpolis = models.BigIntegerField(blank=True, null=True)
    spolis = models.CharField(max_length=10, blank=True, null=True)
    npolis = models.CharField(max_length=20, blank=True, null=True)
    st_okato = models.CharField(max_length=15, blank=True, null=True)
    smo = models.CharField(max_length=5, blank=True, null=True)
    smo_ogrn = models.CharField(max_length=15, blank=True, null=True)
    smo_ok = models.CharField(max_length=5, blank=True, null=True)
    smo_nam = models.CharField(max_length=50, blank=True, null=True)
    novor = models.CharField(max_length=8, blank=True, null=True)
    vnov_d = models.CharField(max_length=10, blank=True, null=True)
    glpu = models.CharField(max_length=6)
    period = models.DateField()

    class Meta:
        managed = False
        db_table = 'xml_pacient_ext'


class XmlSchet(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    glpu = models.CharField(primary_key=True, max_length=6)
    yer = models.CharField(max_length=6, blank=True, null=True)
    mont = models.CharField(max_length=2, blank=True, null=True)
    nschet = models.CharField(max_length=15, blank=True, null=True)
    dschet = models.DateField(blank=True, null=True)
    plat = models.CharField(max_length=10, blank=True, null=True)
    summav = models.FloatField(blank=True, null=True)
    coments = models.CharField(max_length=250, blank=True, null=True)
    sank_mek = models.FloatField(blank=True, null=True)
    sank_mee = models.FloatField(blank=True, null=True)
    summap = models.FloatField(blank=True, null=True)
    sank_ekmp = models.FloatField(blank=True, null=True)
    period = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'xml_schet'
        unique_together = (('glpu', 'period'),)


class XmlSluch(models.Model):
    id_pac = models.CharField(max_length=30, blank=True, null=True)
    idcase = models.CharField(max_length=36, blank=True, null=True)
    pr_nov = models.BigIntegerField(blank=True, null=True)
    usl_ok = models.BigIntegerField(blank=True, null=True)
    vidpom = models.BigIntegerField(blank=True, null=True)
    novor = models.BigIntegerField(blank=True, null=True)
    npr_mo = models.CharField(max_length=6, blank=True, null=True)
    order_field = models.BigIntegerField(db_column='order_', blank=True, null=True)  # Field renamed because it ended with '_'.
    t_order = models.BigIntegerField(blank=True, null=True)
    nhistory = models.CharField(max_length=50, blank=True, null=True)
    date_1 = models.DateField(blank=True, null=True)
    date_2 = models.DateField(blank=True, null=True)
    ds0 = models.CharField(max_length=10, blank=True, null=True)
    ds1 = models.CharField(max_length=10, blank=True, null=True)
    ds2 = models.CharField(max_length=10, blank=True, null=True)
    code_mes1 = models.CharField(max_length=16, blank=True, null=True)
    code_mes2 = models.CharField(max_length=16, blank=True, null=True)
    rslt = models.BigIntegerField(blank=True, null=True)
    ishod = models.BigIntegerField(blank=True, null=True)
    prvs_s = models.CharField(max_length=15, blank=True, null=True)
    iddokt = models.CharField(max_length=15, blank=True, null=True)
    os_sluch = models.BigIntegerField(blank=True, null=True)
    idsp = models.BigIntegerField(blank=True, null=True)
    sumv = models.FloatField(blank=True, null=True)
    oplata = models.BigIntegerField(blank=True, null=True)
    sump = models.FloatField(blank=True, null=True)
    refreason = models.BigIntegerField(blank=True, null=True)
    sank_meks = models.FloatField(blank=True, null=True)
    sank_mees = models.FloatField(blank=True, null=True)
    sank_ekmps = models.FloatField(blank=True, null=True)
    kem_prov = models.BigIntegerField(blank=True, null=True)
    smo = models.CharField(max_length=5, blank=True, null=True)
    id_sluch_tt = models.CharField(max_length=38, blank=True, null=True)
    data_l = models.CharField(max_length=6, blank=True, null=True)
    prizn_prov = models.BigIntegerField(blank=True, null=True)
    tip_exp = models.BigIntegerField(blank=True, null=True)
    kod_exp = models.CharField(max_length=6, blank=True, null=True)
    dat_prov = models.DateField(blank=True, null=True)
    disp = models.CharField(max_length=3, blank=True, null=True)
    vid_hmp = models.CharField(max_length=13, blank=True, null=True)
    metod_hmp = models.CharField(max_length=3, blank=True, null=True)
    ds3 = models.CharField(max_length=10, blank=True, null=True)
    vnov_m = models.FloatField(blank=True, null=True)
    rslt_d = models.BigIntegerField(blank=True, null=True)
    very_spec = models.CharField(max_length=10, blank=True, null=True)
    vbr = models.BigIntegerField(blank=True, null=True)
    p_otk = models.BigIntegerField(blank=True, null=True)
    nrisoms = models.BigIntegerField(blank=True, null=True)
    ds1_pr = models.BigIntegerField(blank=True, null=True)
    naz_sp = models.BigIntegerField(blank=True, null=True)
    naz_v = models.BigIntegerField(blank=True, null=True)
    naz_pmp = models.BigIntegerField(blank=True, null=True)
    naz_pk = models.BigIntegerField(blank=True, null=True)
    pr_d_n = models.BigIntegerField(blank=True, null=True)
    glpu = models.CharField(max_length=6, blank=True, null=True)
    mcod = models.CharField(max_length=6, blank=True, null=True)
    for_pom = models.CharField(max_length=10, blank=True, null=True)
    extr = models.CharField(max_length=10, blank=True, null=True)
    podr = models.CharField(max_length=10, blank=True, null=True)
    profil = models.CharField(max_length=50, blank=True, null=True)
    det = models.BigIntegerField(blank=True, null=True)
    vers_spec = models.CharField(max_length=15, blank=True, null=True)
    ds4 = models.CharField(max_length=7, blank=True, null=True)
    nazn = models.CharField(max_length=15, blank=True, null=True)
    comentsl = models.CharField(max_length=100, blank=True, null=True)
    ed_col = models.FloatField(blank=True, null=True)
    tarif = models.FloatField(blank=True, null=True)
    tal_d = models.DateField(blank=True, null=True)
    tal_p = models.DateField(blank=True, null=True)
    stat = models.BigIntegerField(blank=True, null=True)
    npr_date = models.DateField(blank=True, null=True)
    tal_num = models.CharField(max_length=18, blank=True, null=True)
    period = models.DateField()

    class Meta:
        managed = False
        db_table = 'xml_sluch'


class XmlUsl(models.Model):
    id_sluch = models.CharField(max_length=38, blank=True, null=True)
    idserv = models.CharField(max_length=38)
    lpu = models.CharField(max_length=6)
    lpu_1 = models.CharField(max_length=6, blank=True, null=True)
    podr = models.CharField(max_length=10, blank=True, null=True)
    profil = models.BigIntegerField(blank=True, null=True)
    det = models.BigIntegerField(blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    ds = models.CharField(max_length=10, blank=True, null=True)
    code_mes = models.CharField(max_length=16, blank=True, null=True)
    code_usl = models.CharField(max_length=16, blank=True, null=True)
    ed_col = models.FloatField(blank=True, null=True)
    kol_usl = models.FloatField(blank=True, null=True)
    tarif = models.FloatField(blank=True, null=True)
    sumv_usl = models.FloatField(blank=True, null=True)
    sumv_oms = models.FloatField(blank=True, null=True)
    sumv_sof = models.FloatField(blank=True, null=True)
    sumv_mod = models.FloatField(blank=True, null=True)
    tar_dost = models.FloatField(blank=True, null=True)
    tar_mes = models.FloatField(blank=True, null=True)
    sump_oms = models.FloatField(blank=True, null=True)
    sump_sof = models.FloatField(blank=True, null=True)
    sump_mod = models.FloatField(blank=True, null=True)
    zak = models.BigIntegerField(blank=True, null=True)
    prvs_u = models.CharField(max_length=9, blank=True, null=True)
    code_md = models.CharField(max_length=16, blank=True, null=True)
    sump_p = models.FloatField(blank=True, null=True)
    stand = models.BigIntegerField(blank=True, null=True)
    smo = models.CharField(max_length=5, blank=True, null=True)
    vid_vme = models.CharField(max_length=15, blank=True, null=True)
    koefk = models.FloatField(blank=True, null=True)
    pouh = models.BigIntegerField(blank=True, null=True)
    spolis = models.CharField(max_length=10, blank=True, null=True)
    npolis = models.CharField(max_length=30, blank=True, null=True)
    dir2 = models.BigIntegerField(blank=True, null=True)
    gr_zdorov = models.BigIntegerField(blank=True, null=True)
    student = models.BigIntegerField(blank=True, null=True)
    ot_mes = models.BigIntegerField(blank=True, null=True)
    ot_god = models.BigIntegerField(blank=True, null=True)
    comentu = models.CharField(max_length=100, blank=True, null=True)
    p_per = models.CharField(max_length=10, blank=True, null=True)
    npl = models.CharField(max_length=10, blank=True, null=True)
    idsh = models.CharField(max_length=10, blank=True, null=True)
    id_pac = models.CharField(max_length=38, blank=True, null=True)
    stat = models.FloatField(blank=True, null=True)
    period = models.DateField()

    class Meta:
        managed = False
        db_table = 'xml_usl'


class XmlVrach(models.Model):
    kod = models.CharField(max_length=15)
    fio = models.CharField(max_length=60, blank=True, null=True)
    mcod = models.CharField(max_length=6)
    idmsp = models.CharField(max_length=10, blank=True, null=True)
    spec = models.CharField(max_length=60, blank=True, null=True)
    dost = models.BigIntegerField(blank=True, null=True)
    glpu = models.CharField(max_length=10)
    period = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'xml_vrach'
        unique_together = (('id', 'kod', 'mcod', 'period'),)
