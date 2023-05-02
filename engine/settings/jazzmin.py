JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'E-Soma Admin',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'E-Soma ',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # 'site_logo': 'images/avatar/ava.jpg',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to E-Soma ',

    # Copyright on the footer
    'copyright': 'Antonnifo',

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'courses.Course',

    # Field name on user model that contains avatar image
    'user_avatar': None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},

        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        # {'name': 'Site', 'url': 'https://www.citizenweekly.org/', 'new_window': True},

        # model admin to link to (Permissions checked against model)
        # {'model': 'blog.Post'},
        # {'model': 'auth.User'},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'courses'},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [

        {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': True,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': ['auth.group'],

    # List of apps to base side menu ordering off of (does not need to contain all apps)
    'order_with_respect_to': [''],

    # Custom links to append to app groups, keyed on app name
    # 'custom_links': {
    #     'polls': [{
    #         'name': 'Make Messages', 
    #         'url': 'make_messages', 
    #         'icon': 'fas fa-comments',
    #         'permissions': ['polls.view_poll']
    #     }]
    # },

    # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    # for a list of icon classes
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        # 'website.Comment': 'fas fa-comment-dots',

    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fab fa-pied-piper-alt',

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "carousel",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
    # Add a language dropdown into the admin
    "language_chooser": False,
}