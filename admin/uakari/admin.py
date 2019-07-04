from django.contrib import admin
from django.contrib import messages
from uakari.models import Record, OneRecord


class RecordAdmin(admin.ModelAdmin):
    fields = ('name', 'initial_file', 'max_hash_length', 'expire_at')
    list_display = ('name', 'status', 'num_links', 'result_file')

    def save_model(self, request, obj, form, change):
        super(RecordAdmin, self).save_model(request, obj, form, change)
        obj.send_task()

    def has_delete_permission(self, request, obj=None):
        return False


class OneRecordAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return OneRecord.objects.none()

    def message_user(self, request, message, level=messages.INFO, extra_tags='',
                     fail_silently=False):
        if 'was added successfully' not in message:
            super().message_user(request, message, level, extra_tags, fail_silently)

    def save_model(self, request, obj, form, change):
        short_url = obj.write_to_redis()
        self.message_user(request,f'Short url: www.sitename.ru/{short_url}',)


admin.site.disable_action('delete_selected')
admin.site.register(Record, RecordAdmin)
admin.site.register(OneRecord, OneRecordAdmin)
