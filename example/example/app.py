from pecan import make_app

from example import model
from example.common.hooks import GlobalHandlerHooks


def setup_app(config):
    model.init_model()
    app_conf = dict(config.app)

    app = make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=[GlobalHandlerHooks()],
        force_canonical=False,
        **app_conf
    )

    return app
