# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table('jobs_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('hours', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('salary', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_contact', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('jobs', ['Job'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table('jobs_job')


    models = {
        'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'company_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['jobs']