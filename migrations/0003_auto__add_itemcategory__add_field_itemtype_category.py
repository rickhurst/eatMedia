# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemCategory'
        db.create_table('eatMedia_itemcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('eatMedia', ['ItemCategory'])

        # Adding field 'ItemType.category'
        db.add_column('eatMedia_itemtype', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eatMedia.ItemCategory'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ItemCategory'
        db.delete_table('eatMedia_itemcategory')

        # Deleting field 'ItemType.category'
        db.delete_column('eatMedia_itemtype', 'category_id')


    models = {
        'eatMedia.folder': {
            'Meta': {'object_name': 'Folder'},
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'eatMedia.item': {
            'Meta': {'object_name': 'Item'},
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eatMedia.Folder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eatMedia.ItemType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'eatMedia.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'eatMedia.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eatMedia.ItemCategory']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eatMedia']