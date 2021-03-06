from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('content_store.views',
  (r'^new-store/(?P<store_name>[^/]+)/?$',                                               'newStore'),
  (r'^regenerate-api-key/(?P<store_name>[^/]+)/?$',                                      'regenerate_api_key'),
  (r'^open-store/(?P<store_name>[^/]+)/?$',                                              'openStore'),
  (r'^delete-store/(?P<store_name>[^/]+)/?$',                                            'deleteStore'),
  (r'^purge-store/(?P<store_name>[^/]+)/?$',                                             'purgeStore'),
  (r'^exists/(?P<store_name>[^/]+)/?$',                                                  'storeExists'),
  (r'^(?P<store_name>[^/]+)/load-index/?$',                                              'load_index'),
  (r'^(?P<store_name>[^/]+)/with-running-info/?$',                                       'with_running_info'),
  (r'^(?P<store_name>[^/]+)/cluster-svg/?$',                                             'cluster_svg'),
  (r'^(?P<store_name>[^/]+)/update-schema/(?P<config_id>[^/]+)/?$',                      'updateSchema'),
  (r'^(?P<store_name>[^/]+)/update-properties/(?P<config_id>[^/]+)/?$',                  'updateProperties'),
  (r'^(?P<store_name>[^/]+)/update-custom-facets/(?P<config_id>[^/]+)/?$',               'updateCustomFacets'),
  (r'^(?P<store_name>[^/]+)/update-plugins/(?P<config_id>[^/]+)/?$',                     'updatePlugins'),
  (r'^(?P<store_name>[^/]+)/update-vm-args/(?P<config_id>[^/]+)/?$',                     'updateVMArgs'),
  (r'^(?P<store_name>[^/]+)/update-name/(?P<config_id>[^/]+)/?$',                        'updateName'),
  (r'^(?P<store_name>[^/]+)/delete-config/(?P<config_id>[^/]+)/?$',                      'deleteConfig'),
  (r'^(?P<store_name>[^/]+)/export-config/(?P<config_id>[^/]+)/(?P<file_name>[^/]+)/?$', 'export_config'),
  (r'^(?P<store_name>[^/]+)/import-config/?$',                                           'import_config'),
  (r'^(?P<store_name>[^/]+)/config/(?P<config_id>[^/]+)/extensions/?$',                  'configExtensions'),
  (r'^(?P<store_name>[^/]+)/config/(?P<config_id>[^/]+)/update-extensions/?$',           'updateExtensions'),
  (r'^add-docs/(?P<store_name>[^/]+)/?$',                                                'addDocs'),
  (r'^update-doc/(?P<store_name>[^/]+)/?$',                                              'updateDoc'),
  (r'^start-store/(?P<store_name>[^/]+)/?(?P<config_id>[^/]+)?/?$',                      'startStore'),
  (r'^stop-store/(?P<store_name>[^/]+)/?$',                                              'stopStore'),
  (r'^restart-store/(?P<store_name>[^/]+)/?(?P<config_id>[^/]+)?/?$',                    'restartStore'),
  (r'^get-size/(?P<store_name>[^/]+)/?$',                                                'getSize'),
  (r'^get-doc/(?P<id>\d+)/(?P<store_name>[^/]+)/?$',                                     'getDoc'),
  (r'^delete-docs/(?P<store_name>[^/]+)/?$',                                             'delDocs'),
  (r'^available/(?P<store_name>[^/]+)/?$',                                               'available'),
  (r'^collaborators/(?P<store_name>[^/]+)/?$',                                           'collaborators'),
  (r'^configs/(?P<store_name>[^/]+)/?$',                                                 'configs'),
  (r'^add-collab/(?P<store_name>[^/]+)/?$',                                              'add_collab'),
  (r'^remove-collab/(?P<store_name>[^/]+)/?$',                                           'remove_collab'),
  (r'^stores/?$',                                                                        'stores'),
)
