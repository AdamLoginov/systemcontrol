from django.contrib import admin


# for User 
from SysControl.models import Entry

class EntryAdmin(admin.ModelAdmin):

    # Поля, доступные для редактирования простым пользователям.
    # Разрешаем только title
    user_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',)
        }),
    )

    list_display = ['title', 'user']
    raw_id_list_displayfields = ('user',)
    search_fields = ['title', 'user__username']

    # автозаполнение поля юзер
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not request.user.is_superuser or not form.cleaned_data["user"]:
                obj.user = request.user
                obj.save()
            elif form.cleaned_data["user"]:
                obj.user = form.cleaned_data["user"]
                obj.save()

    # добавляет колонку юзер в список объектов 
    def preprocess_list_display(self, request):
        if 'user' not in self.list_display:
            self.list_display.insert(self.list_display.__len__(), 'user')
        if not request.user.is_superuser:
            if 'user' in self.list_display:
                self.list_display.remove('user')

    # 
    def preprocess_search_fields(self, request):
        if 'user__username' not in self.search_fields:
            self.search_fields.insert(self.search_fields.__len__(), 'user__username')
        if not request.user.is_superuser:
            if 'user__username' in self.search_fields:
                self.search_fields.remove('user__username')

    def changelist_view(self, request, extra_context=None):
        self.preprocess_list_display(request)
        self.preprocess_search_fields(request)
        return super(EntryAdmin, self).changelist_view(request)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(EntryAdmin, self).get_queryset(request)
        else:
            qs = super(EntryAdmin, self).get_queryset(request)
            return qs.filter(user=request.user)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super(EntryAdmin, self).get_fieldsets(request, obj)
        return self.user_fieldsets

admin.site.register(Entry, EntryAdmin)

