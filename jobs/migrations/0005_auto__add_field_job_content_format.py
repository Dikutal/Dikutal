# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Job.content_format'
        db.add_column('jobs_job', 'content_format',
                      self.gf('django.db.models.fields.CharField')(default='MD', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Job.content_format'
        db.delete_column('jobs_job', 'content_format')


    models = {
        'jobs.company': {
            'Meta': {'object_name': 'Company'},
            'company_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jobs.Company']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "'MD'", 'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'jobs.jobfeed': {
            'Meta': {'object_name': 'JobFeed'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jobs']