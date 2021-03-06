from django.conf.urls import include, patterns, url


urlpatterns = patterns('misago.users.views.auth',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)


urlpatterns += patterns('misago.users.views.register',
    url(r'^register/$', 'register', name='register'),
    url(r'^register/completed/$', 'register_completed', name='register_completed'),
)


urlpatterns += patterns('misago.users.views.activation',
    url(r'^activation/request/$', 'request_activation', name="request_activation"),
    url(r'^activation/sent/$', 'activation_sent', name="activation_sent"),
    url(r'^activation/(?P<user_id>\d+)/(?P<token>[a-zA-Z0-9]+)/$', 'activate_by_token', name="activate_by_token"),
)


urlpatterns += patterns('misago.users.views.forgottenpassword',
    url(r'^forgotten-password/$', 'request_reset', name='request_password_reset'),
    url(r'^forgotten-password/link-sent/$', 'link_sent', name='reset_password_link_sent'),
    url(r'^forgotten-password/(?P<user_id>\d+)/(?P<token>[a-zA-Z0-9]+)/$', 'reset_password_form', name='reset_password_form'),
)


urlpatterns += patterns('misago.users.views.api',
    url(r'^api/validate/username/$', 'validate_username', name='api_validate_username'),
    url(r'^api/validate/username/(?P<user_id>\d+)/$', 'validate_username', name='api_validate_username'),
    url(r'^api/validate/email/$', 'validate_email', name='api_validate_email'),
    url(r'^api/validate/email/(?P<user_id>\d+)/$', 'validate_email', name='api_validate_email'),
    url(r'^api/validate/password/$', 'validate_password', name='api_validate_password'),
    url(r'^api/suggestion-engine/$', 'suggestion_engine', name='api_suggestion_engine'),
)


urlpatterns += patterns('misago.users.views.usercp',
    url(r'^usercp/forum-options/$', 'change_forum_options', name="usercp_change_forum_options"),
    url(r'^usercp/change-avatar/$', 'change_avatar', name="usercp_change_avatar"),
    url(r'^usercp/change-avatar/upload/$', 'upload_avatar', name="usercp_upload_avatar"),
    url(r'^usercp/change-avatar/upload/handle/$', 'upload_avatar_handler', name="usercp_upload_avatar_handler"),
    url(r'^usercp/change-avatar/upload/crop/$', 'crop_avatar', name="usercp_crop_new_avatar", kwargs={'use_tmp_avatar': True}),
    url(r'^usercp/change-avatar/crop/$', 'crop_avatar', name="usercp_crop_avatar", kwargs={'use_tmp_avatar': False}),
    url(r'^usercp/change-avatar/galleries/$', 'avatar_galleries', name="usercp_avatar_galleries"),
    url(r'^usercp/edit-signature/$', 'edit_signature', name="usercp_edit_signature"),
    url(r'^usercp/change-username/$', 'change_username', name="usercp_change_username"),
    url(r'^usercp/change-email-password/$', 'change_email_password', name="usercp_change_email_password"),
    url(r'^usercp/change-email-password/(?P<token>[a-zA-Z0-9]+)/$', 'confirm_email_password_change', name='usercp_confirm_email_password_change'),
)


urlpatterns += patterns('',
    url(r'^users/', include(patterns('misago.users.views.lists',
        url(r'^$', 'lander', name="users"),
        url(r'^active-posters/$', 'active_posters', name="users_active_posters"),
        url(r'^active-posters/(?P<page>\d+)/$', 'active_posters', name="users_active_posters"),
        url(r'^online/$', 'online', name="users_online"),
        url(r'^online/(?P<page>\d+)/$', 'online', name="users_online"),
        url(r'^(?P<rank_slug>[-a-zA-Z0-9]+)/$', 'rank', name="users_rank"),
        url(r'^(?P<rank_slug>[-a-zA-Z0-9]+)/(?P<page>\d+)/$', 'rank', name="users_rank"),
    )))
)


urlpatterns += patterns('',
    url(r'^user/(?P<user_slug>[a-zA-Z0-9]+)-(?P<user_id>\d+)/', include(patterns('misago.users.views.profile',
        url(r'^$', 'posts', name="user_posts"),
        url(r'^threads/$', 'threads', name="user_threads"),
        url(r'^followers/$', 'followers', name="user_followers"),
        url(r'^followers/(?P<page>\d+)/$', 'followers', name="user_followers"),
        url(r'^follows/$', 'follows', name="user_follows"),
        url(r'^follows/(?P<page>\d+)/$', 'follows', name="user_follows"),
        url(r'^name-history/$', 'name_history', name="user_name_history"),
        url(r'^name-history/(?P<page>\d+)/$', 'name_history', name="user_name_history"),
        url(r'^warnings/$', 'warnings', name="user_warnings"),
        url(r'^warnings/(?P<page>\d+)/$', 'warnings', name="user_warnings"),
        url(r'^ban-details/$', 'user_ban', name="user_ban"),

        url(r'^follow/$', 'follow_user', name="follow_user"),
        url(r'^block/$', 'block_user', name="block_user"),
    )))
)


urlpatterns += patterns('',
    url(r'^mod-user/(?P<user_slug>[a-zA-Z0-9]+)-(?P<user_id>\d+)/', include(patterns('misago.users.views.moderation',
        url(r'^warn/$', 'warn', name='warn_user'),
        url(r'^warn/(?P<warning_id>\d+)/cancel/$', 'cancel_warning', name='cancel_warning'),
        url(r'^warn/(?P<warning_id>\d+)/delete/$', 'delete_warning', name='delete_warning'),
        url(r'^rename/$', 'rename', name='rename_user'),
        url(r'^avatar/$', 'moderate_avatar', name='moderate_avatar'),
        url(r'^signature/$', 'moderate_signature', name='moderate_signature'),
        url(r'^ban/$', 'ban_user', name='ban_user'),
        url(r'^lift-ban/$', 'lift_user_ban', name='lift_user_ban'),
        url(r'^delete/$', 'delete', name='delete_user'),
    ))),
)


urlpatterns += patterns('',
    url(r'^user-avatar/', include(patterns('misago.users.views.avatarserver',
        url(r'^(?P<size>\d+)/(?P<user_id>\d+)\.png$', 'serve_user_avatar', name="user_avatar"),
        url(r'^tmp:(?P<token>[a-zA-Z0-9]+)/(?P<user_id>\d+)\.png$', 'serve_user_avatar_source', name="user_avatar_tmp", kwargs={'type': 'tmp'}),
        url(r'^org:(?P<token>[a-zA-Z0-9]+)/(?P<user_id>\d+)\.png$', 'serve_user_avatar_source', name="user_avatar_org", kwargs={'type': 'org'}),
        url(r'^(?P<size>\d+)\.png$', 'serve_blank_avatar', name="blank_avatar"),
    )))
)
