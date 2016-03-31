import copernicus_api

LIGHT = copernicus_api.QueryableComponent.LIGHT
BUTTON1 = copernicus_api.QueryableComponent.BUTTON1
BUTTON2 = copernicus_api.QueryableComponent.BUTTON2
KNOB = copernicus_api.QueryableComponent.KNOB
TEMP = copernicus_api.QueryableComponent.TEMP
MOTION = copernicus_api.QueryableComponent.MOTION


def set_dash(angle):
    req = copernicus_api.Request.to_set_dashboard_angle(angle)
    copernicus_api.Copernicus().send_request(req)


def set_led1(value):
    req = copernicus_api.Request.to_set_led1(value)
    copernicus_api.Copernicus().send_request(req)


def set_led2(r, g, b):
    req = copernicus_api.Request.to_set_rgb_of_led2(copernicus_api.Rgb3(r, g, b))
    copernicus_api.Copernicus().send_request(req)


def subscribe(*args):
    req = copernicus_api.Request.for_automatic_updates_of(args)
    copernicus_api.Copernicus().send_request(req)


def query(*args):
    req = copernicus_api.Request.query_for_parameters_of(args)
    copernicus_api.Copernicus().send_request(req)


def get_res():
    copernicus_api.Copernicus().get_response()
