# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Presentation'
        db.create_table('core_presentation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('core', ['Presentation'])

        # Adding unique constraint on 'Presentation', fields ['type', 'language']
        db.create_unique('core_presentation', ['type', 'language'])

        # Adding model 'SocialNetwork'
        db.create_table('core_socialnetwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('core', ['SocialNetwork'])

        # Adding model 'Work'
        db.create_table('core_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('core', ['Work'])

        # Adding unique constraint on 'Work', fields ['slug', 'language']
        db.create_unique('core_work', ['slug', 'language'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Work', fields ['slug', 'language']
        db.delete_unique('core_work', ['slug', 'language'])

        # Removing unique constraint on 'Presentation', fields ['type', 'language']
        db.delete_unique('core_presentation', ['type', 'language'])

        # Deleting model 'Presentation'
        db.delete_table('core_presentation')

        # Deleting model 'SocialNetwork'
        db.delete_table('core_socialnetwork')

        # Deleting model 'Work'
        db.delete_table('core_work')


    models = {
        'core.presentation': {
            'Meta': {'unique_together': "(('type', 'language'),)", 'object_name': 'Presentation'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.socialnetwork': {
            'Meta': {'object_name': 'SocialNetwork'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'core.work': {
            'Meta': {'unique_together': "(('slug', 'language'),)", 'object_name': 'Work'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
