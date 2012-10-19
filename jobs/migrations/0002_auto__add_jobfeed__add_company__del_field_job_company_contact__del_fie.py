# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobFeed'
        db.create_table('jobs_jobfeed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('last_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('jobs', ['JobFeed'])

        # Adding model 'Company'
        db.create_table('jobs_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_contact', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('company_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('jobs', ['Company'])

        # Deleting field 'Job.company_contact'
        db.delete_column('jobs_job', 'company_contact')

        # Deleting field 'Job.company_phone'
        db.delete_column('jobs_job', 'company_phone')

        # Deleting field 'Job.company_description'
        db.delete_column('jobs_job', 'company_description')

        # Deleting field 'Job.company_address'
        db.delete_column('jobs_job', 'company_address')

        # Deleting field 'Job.company_name'
        db.delete_column('jobs_job', 'company_name')

        # Deleting field 'Job.company_email'
        db.delete_column('jobs_job', 'company_email')

        # Adding field 'Job.company'
        db.add_column('jobs_job', 'company',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['jobs.Company']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'JobFeed'
        db.delete_table('jobs_jobfeed')

        # Deleting model 'Company'
        db.delete_table('jobs_company')

        # Adding field 'Job.company_contact'
        db.add_column('jobs_job', 'company_contact',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Job.company_phone'
        db.add_column('jobs_job', 'company_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Job.company_description'
        db.add_column('jobs_job', 'company_description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Job.company_address'
        db.add_column('jobs_job', 'company_address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Job.company_name'
        db.add_column('jobs_job', 'company_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Job.company_email'
        db.add_column('jobs_job', 'company_email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'Job.company'
        db.delete_column('jobs_job', 'company_id')


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
            'address': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jobs.Company']"}),
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
        },
        'jobs.jobfeed': {
            'Meta': {'object_name': 'JobFeed'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jobs']