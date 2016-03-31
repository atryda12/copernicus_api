import copernicus_api

LIGHT = copernicus_api.QueryableComponent.LIGHT
BUTTON1 = copernicus_api.QueryableComponent.BUTTON1
BUTTON2 = copernicus_api.QueryableComponent.BUTTON2
KNOB = copernicus_api.QueryableComponent.KNOB
TEMP = copernicus_api.QueryableComponent.TEMP
MOTION = copernicus_api.QueryableComponent.MOTION


def set_dash(angle):
    copernicus_api.Request.to_set_dashboard_angle(angle)


def set_led1(value):
    copernicus_api.Request.to_set_led1(value)


def set_led2(r, g, b):
    copernicus_api.Request.to_set_rgb_of_led2(copernicus_api.Rgb3(r, g, b))


def subscribe(*args):
    copernicus_api.Request.for_automatic_updates_of(args)


def query(*args):
    copernicus_api.Request.query_for_parameters_of(args)


def req(request):
    copernicus_api.Copernicus().send_request(request)


def get_res():
    copernicus_api.Copernicus().get_response()
