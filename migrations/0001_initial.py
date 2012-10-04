# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Folder'
        db.create_table('eatMedia_folder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('eatMedia', ['Folder'])

        # Adding model 'ItemType'
        db.create_table('eatMedia_itemtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('eatMedia', ['ItemType'])

        # Adding model 'Item'
        db.create_table('eatMedia_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eatMedia.Folder'])),
            ('item_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eatMedia.ItemType'])),
        ))
        db.send_create_signal('eatMedia', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Folder'
        db.delete_table('eatMedia_folder')

        # Deleting model 'ItemType'
        db.delete_table('eatMedia_itemtype')

        # Deleting model 'Item'
        db.delete_table('eatMedia_item')


    models = {
        'eatMedia.folder': {
            'Meta': {'object_name': 'Folder'},
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'eatMedia.item': {
            'Meta': {'object_name': 'Item'},
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eatMedia.Folder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eatMedia.ItemType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'eatMedia.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eatMedia']