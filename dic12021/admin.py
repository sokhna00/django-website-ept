from django.contrib.admin import AdminSite


class AdminSiteDIC12021(AdminSite):
    site_header = 'Administration site EPT'
    site_title = 'EPT'
    empty_value_display = 'null'


admin_dic = AdminSiteDIC12021(name='admindic')