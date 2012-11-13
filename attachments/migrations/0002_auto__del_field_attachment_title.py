# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Attachment.title'
        db.delete_column('attachments_attachment', 'title')


    def backwards(self, orm):
        # Adding field 'Attachment.title'
        db.add_column('attachments_attachment', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)


    models = {
        'attachments.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['attachments']