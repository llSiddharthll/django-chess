from chess_engine.models import UserColorSet

""" themes """
available_themes = [
    {'name': 'alpen', 'label': 'Alpen', 'file_name': 'bootstrap-alpen.css'},
    {'name': 'gluestudio', 'label': 'Glue Studio', 'file_name': 'bootstrap-GlueStudio.css'},
    {'name': 'dream_magnet', 'label': 'Dream Magnet', 'file_name': 'bootstrap-lagunabeach-dream-magnet.css'},
    {'name': 'miss_anthropy', 'label': 'Miss Anthropy', 'file_name': 'bootstrap-Miss-Anthropy.css'},
    {'name': 'sugar', 'label': 'Sugar', 'file_name': 'bootstrap-Sugar.css'},
    {'name': 'mystery_machine', 'label': 'Mistery Machine', 'file_name': 'bootstrap-valeryanaglz-mystery-machine.css', 'required_level': 1},
    {'name': 'yasmino', 'label': 'Yasmino', 'file_name': 'bootstrap-Yasmino.css', 'required_level': 2},
    {'name': 'good_friends', 'label': 'Good Friends', 'file_name': 'bootstrap-Yasmino-Good-Friends.css', 'required_level': 3},
]

available_pieces = [
    {'name': 'default', 'label': 'Default', 'folder_name': 'default'},
    {'name': 'set_1', 'label': 'Set 1', 'folder_name': 'set_1', 'required_level': 1},
]


def add_generic_context(context, request):
    context['user_theme'] = get_user_theme(request.user)
    context['user_pieces'] = get_user_pieces(request.user)


def add_theme_list(context):
    context['available_themes'] = get_themes_list()
    context['available_pieces'] = get_pieces_list()


def get_themes_list():
    return available_themes


def get_pieces_list():
    return available_pieces


def get_user_theme(user):
    user_color_set = UserColorSet.objects.filter(user=user).first()
    if not user_color_set:
        return dict()
    theme_name = user_color_set.get_data('main/theme')
    if not theme_name:
        return dict()

    for theme in available_themes:
        if theme['name'] == theme_name:
            return theme
    return dict()


def get_user_pieces(user):
    user_color_set = UserColorSet.objects.filter(user=user).first()
    if not user_color_set:
        return dict()
    user_pieces_name = user_color_set.get_data('main/piece_set')
    if not user_pieces_name:
        return available_pieces[0]

    for piece_set in available_pieces:
        if piece_set['name'] == user_pieces_name:
            return piece_set
    return dict()
