# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Spot.external_id'
        db.add_column('spotseeker_server_spot', 'external_id',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Spot.external_id'
        db.delete_column('spotseeker_server_spot', 'external_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oauth_provider.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'spotseeker_server.spot': {
            'Meta': {'object_name': 'Spot'},
            'building_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'display_access_restrictions': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'external_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'floor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'height_from_sea_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8'}),
            'manager': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'spottypes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'spots'", 'max_length': '50', 'to': "orm['spotseeker_server.SpotType']"})
        },
        'spotseeker_server.spotavailablehours': {
            'Meta': {'object_name': 'SpotAvailableHours'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spotseeker_server.Spot']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'spotseeker_server.spotextendedinfo': {
            'Meta': {'object_name': 'SpotExtendedInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spotseeker_server.Spot']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'spotseeker_server.spotimage': {
            'Meta': {'object_name': 'SpotImage'},
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spotseeker_server.Spot']"}),
            'upload_application': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'upload_user': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'spotseeker_server.spottype': {
            'Meta': {'object_name': 'SpotType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'spotseeker_server.trustedoauthclient': {
            'Meta': {'object_name': 'TrustedOAuthClient'},
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth_provider.Consumer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_trusted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['spotseeker_server']